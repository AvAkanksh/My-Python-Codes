import time
import requests
import os
from playwright.sync_api import sync_playwright
from PIL import Image

# --- CONFIGURATION ---
OUTPUT_DIR = "leetcode_captures"
PDF_NAME = "LeetCode_Questions_Fixed.pdf"
LIMIT_QUESTIONS = 5 

def get_problem_list():
    print("Fetching problem list...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://leetcode.com/api/problems/algorithms/", headers=headers)
        data = resp.json()
        
        problems = []
        for q in data["stat_status_pairs"]:
            if not q["paid_only"]:
                problems.append({
                    "id": int(q["stat"]["frontend_question_id"]),
                    "title": q["stat"]["question__title"],
                    "slug": q["stat"]["question__title_slug"]
                })
        
        problems.sort(key=lambda x: x["id"])
        return problems[:LIMIT_QUESTIONS] if LIMIT_QUESTIONS else problems
    except Exception as e:
        print(f"API Error: {e}")
        return []

def capture_questions():
    problems = get_problem_list()
    if not problems:
        return []

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with sync_playwright() as p:
        # Launch options (Manjaro friendly)
        browser = p.chromium.launch(headless=False)
        
        # VERY TALL viewport to ensure the whole question fits without scrolling
        context = browser.new_context(viewport={"width": 1600, "height": 2000})
        page = context.new_page()

        image_files = []

        for p_data in problems:
            slug = p_data["slug"]
            full_title = f"{p_data['id']}. {p_data['title']}" 
            url = f"https://leetcode.com/problems/{slug}/description/"
            
            print(f"Processing: {full_title}...")
            
            try:
                page.goto(url)
                
                # 1. Wait for Title to ensure page load
                try:
                    page.get_by_text(full_title, exact=False).first.wait_for(timeout=10000)
                except:
                    print(f"   -> Timeout waiting for: {full_title}")
                    continue

                # 2. Cleanup (Hide Navbar)
                page.evaluate("try { document.querySelector('#navbar-root').style.display = 'none'; } catch(e) {}")

                # --- THE FIX: SMART CONTAINER SELECTION ---
                # Strategy: Find a <div> that contains the Title AND contains the text "Example 1"
                # This forces Playwright to select the wrapper that holds both.
                
                # 1. Find all divs that have the Title
                candidates = page.locator("div").filter(has=page.get_by_text(full_title, exact=False))
                
                # 2. Narrow it down to divs that ALSO have "Example 1" (Standard in all LC questions)
                # If "Example 1" is missing (rare), it falls back to "Constraints"
                container = candidates.filter(has=page.get_by_text("Example 1"))
                
                if container.count() == 0:
                     # Fallback: Try looking for "Constraints" if "Example 1" isn't found
                    container = candidates.filter(has=page.get_by_text("Constraints"))

                # 3. Select the LAST match. 
                # (Because HTML is nested: Body -> SplitPane -> QuestionCard. 
                # The 'QuestionCard' is the deepest/last one, which is the tightest crop.)
                final_element = container.last
                
                if final_element.count() > 0:
                    save_path = os.path.join(OUTPUT_DIR, f"{p_data['id']}_{slug}.png")
                    # Screenshot just that container
                    final_element.screenshot(path=save_path)
                    image_files.append(save_path)
                    print(f"   -> Captured (Title + Body).")
                else:
                    print("   -> Could not find common container.")

            except Exception as e:
                print(f"   -> Error on {slug}: {e}")

        browser.close()
        return image_files

def images_to_pdf(image_paths, output_pdf):
    if not image_paths:
        print("No images to merge.")
        return
    print(f"Merging {len(image_paths)} images into PDF...")
    first = Image.open(image_paths[0]).convert("RGB")
    others = [Image.open(img).convert("RGB") for img in image_paths[1:]]
    first.save(output_pdf, save_all=True, append_images=others)
    print(f"Done: {output_pdf}")

if __name__ == "__main__":
    imgs = capture_questions()
    images_to_pdf(imgs, PDF_NAME)
