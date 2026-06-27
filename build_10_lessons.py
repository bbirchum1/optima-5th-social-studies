#!/usr/bin/env python3
"""Build 10 G5 social studies lessons by clean-swapping base templates."""

import os, re

BASE_DIR = "/sessions/awesome-ecstatic-goldberg/mnt/optima-5th-social-studies"

# Read base templates
with open(f"{BASE_DIR}/ss-5-11.01-how-why-us-government-created-constitution.html") as f:
    BASE_FP = f.read()
with open(f"{BASE_DIR}/ss-5-11.02-representative-government-constitutional-republic.html") as f:
    BASE_EB = f.read()
with open(f"{BASE_DIR}/ss-5-10.08-revolutionary-war-campaign-map-timeline.html") as f:
    BASE_SD = f.read()

# ═══════════════════════════════════════════════════════════════
# LESSON DATA
# ═══════════════════════════════════════════════════════════════

LESSONS = []

# Helper to add lessons
def L(d):
    LESSONS.append(d)

L({
    "code": "5.11.03", "code_hyph": "5-11-03",
    "title": "Articles I, II, and III: Powers of the National Government",
    "kebab": "articles-i-ii-iii-powers-national-government",
    "issue": 57, "week": 29, "seq": 57, "circ": 3940,
    "base": "fp",
    "unit_code": "G5-U11", "unit_title": "Constitution and Constitutional Republic",
    "virtue": "Honesty", "virtue_lc": "honesty",
    "standards": "SS.5.CG.1.2; SS.5.CG.1.3; SS.5.CG.1.4; SS.5.CG.2.3; SS.5.CG.2.4; SS.5.CG.2.5; SS.5.CG.3.1; SS.5.CG.3.2; SS.5.CG.3.3; SS.5.CG.3.4; SS.5.CG.3.5; SS.5.CG.3.6; SS.5.HE.1.1",
    "herald_headline": "Three Branches? Just Three Lists!",
    "herald_claim": "The Hasty Herald says the three branches of government are just three lists of government jobs — they all do the same thing.",
    "herald_task": "You'll investigate how the Constitution gives each branch different powers — and why that division matters.",
    "story_phase": "Civic editor's desk: explain constitutional principles, rights, limits, dignity, and responsibility.",
    "socratic": "What decision would serve the common good, and what evidence supports that judgment?",
    "assignment": "Civic Editor's Note",
    "artifact_type": "Front Page Brief",
    "artifact_label": "Front Page Brief",
    "next_code": "5.11.04", "next_title": "Bill of Rights and Limits on Government",
    "next_desk": "Editorial Board",
    "avery_short": "examining how the Constitution divides power among three branches.",
    "beat_label": "Separation of Powers",
    "dispatch": "The Front Page Desk has a new file: <em>5.11.03 — Articles I, II, and III: Powers of the National Government</em>. Last issue, the Editorial Board investigated representative government. Now we go deeper: how does the Constitution actually divide power? The Hasty Herald has already rushed its version to print, claiming the three branches \"are just three lists of government jobs.\"",
    "last_edition_summary": "Last issue, the Editorial Board weighed evidence about <em>representative government</em> and the constitutional republic.",
    "last_edition_archive": "Last issue's Archive Line asked what representative government really means — and why it's more than majority rule.",
    "obj1": "I can identify the three branches of the national government and their main powers.",
    "obj2": "I can explain how the Constitution separates powers among the legislative, executive, and judicial branches.",
    "obj3": "I can describe why the founders believed dividing power would protect citizens' rights.",
    "welcome_notes": "Welcome back, Junior Editors. Last time we explored representative government. Today we open the Constitution itself — Articles I, II, and III — and discover how the founders divided power into three branches. The Herald says they're all the same. Let's investigate.",
    "path_step2": "Examine the three branches",
    "path_step3": "Write your Front Page Brief",
    "virtue_text": "Honesty means reporting the differences — not lumping everything together for a quick headline. The Herald says all three branches do the same thing. An honest editor reads the text and reports the truth.",
    "role_text": "You'll examine Articles I, II, and III of the Constitution to understand how legislative, executive, and judicial powers differ — and why that separation matters.",
    "editors_followup": "Keep this question on your desk as you investigate. Each branch has different powers for a reason. Your job is to explain what each branch does and why dividing power serves the common good.",
    "explore_notes": "Walk students through the three articles: Article I (Congress — makes laws), Article II (President — enforces laws), Article III (Courts — interprets laws). Use simple examples. Emphasize checks and balances.",
    "tab2_content": """
    <div class="content-section">
    <h2>\U0001f5de️ Three Branches, Three Jobs</h2>
    <p>The Hasty Herald says "the three branches of government are just three lists of government jobs." But the Constitution didn't just make a list — it carefully separated power so that no single person or group could control the government. Today at the Front Page Desk, you'll read Articles I, II, and III to discover what each branch does and why the founders designed it this way.</p>

    <div class="callout callout-info" style="border-left-color: var(--gazette-gold);">
      <div class="callout-icon">\U0001f5de️</div>
      <div>
        <strong>Reading the Constitution</strong>
        <p>As you read, notice how each article gives a different branch specific powers — and limits. The founders chose these words carefully.</p>
      </div>
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin:16px 0;">
      <div style="background:var(--paper-cream); border:1.5px solid #C4A672; border-radius:10px; padding:16px; border-top:4px solid #1A2138;">
        <div style="font-family:'Playfair Display',serif; font-weight:800; color:#1A2138; font-size:15px; margin-bottom:8px;">\U0001f4dc Article I — Congress</div>
        <div style="font-family:'Crimson Text',serif; font-size:14px; line-height:1.6; color:var(--ink);">
          <p style="margin:0 0 8px;"><strong>Branch:</strong> Legislative</p>
          <p style="margin:0 0 8px;"><strong>Power:</strong> Makes the laws</p>
          <p style="margin:0 0 8px;">Congress has two parts: the Senate (2 per state) and the House of Representatives (based on population). Only Congress can declare war, collect taxes, and create new laws.</p>
          <p style="margin:0;"><strong>Key limit:</strong> The President can veto bills, and courts can rule laws unconstitutional.</p>
        </div>
      </div>
      <div style="background:var(--paper-cream); border:1.5px solid #C4A672; border-radius:10px; padding:16px; border-top:4px solid #8B2D26;">
        <div style="font-family:'Playfair Display',serif; font-weight:800; color:#8B2D26; font-size:15px; margin-bottom:8px;">\U0001f3db️ Article II — The President</div>
        <div style="font-family:'Crimson Text',serif; font-size:14px; line-height:1.6; color:var(--ink);">
          <p style="margin:0 0 8px;"><strong>Branch:</strong> Executive</p>
          <p style="margin:0 0 8px;"><strong>Power:</strong> Enforces the laws</p>
          <p style="margin:0 0 8px;">The President carries out the laws Congress passes, commands the military, and works with other nations. The President can sign or veto bills.</p>
          <p style="margin:0;"><strong>Key limit:</strong> Congress can override a veto and can impeach the President.</p>
        </div>
      </div>
      <div style="background:var(--paper-cream); border:1.5px solid #C4A672; border-radius:10px; padding:16px; border-top:4px solid #2E6B4A;">
        <div style="font-family:'Playfair Display',serif; font-weight:800; color:#2E6B4A; font-size:15px; margin-bottom:8px;">⚖️ Article III — The Courts</div>
        <div style="font-family:'Crimson Text',serif; font-size:14px; line-height:1.6; color:var(--ink);">
          <p style="margin:0 0 8px;"><strong>Branch:</strong> Judicial</p>
          <p style="margin:0 0 8px;"><strong>Power:</strong> Interprets the laws</p>
          <p style="margin:0 0 8px;">The Supreme Court and federal courts decide whether laws follow the Constitution. Judges serve for life so they can make decisions without political pressure.</p>
          <p style="margin:0;"><strong>Key limit:</strong> The President appoints judges, and the Senate must approve them.</p>
        </div>
      </div>
    </div>

    <div class="callout callout-think">
      <div class="callout-icon">⚖️</div>
      <div>
        <strong>Checks and Balances</strong>
        <p>Notice how each branch can limit the others. Congress makes laws — but the President can veto them. The President enforces laws — but Congress can override a veto. Courts interpret laws — but the President appoints judges. This system of <strong>checks and balances</strong> keeps any one branch from becoming too powerful.</p>
      </div>
    </div>

    <div class="owl-buddy">
      <div class="owl-icon">\U0001f989\U0001f5de️</div>
      <div class="owl-bubble">
        The Herald says all three branches "do the same thing." But look at the evidence: one <em>makes</em> laws, one <em>enforces</em> laws, and one <em>interprets</em> laws. That's three very different jobs — and the founders separated them on purpose.
      </div>
    </div>

    <div class="callout callout-tip">
      <div class="callout-icon">\U0001f4a1</div>
      <div>
        <strong>Key Concept</strong>
        <p>The Constitution separates power into three branches — legislative, executive, and judicial — each with specific powers and limits. This separation protects citizens by preventing any one group from controlling the entire government.</p>
      </div>
    </div>
  </div>
""",
    "notebook_intro": "Write a few sentences for each. These notes will help you write your Front Page Brief on the next tab.",
    "q1_text": "What are the three branches of government, and what is each branch's main job?",
    "q1_placeholder": "The three branches are...",
    "q2_text": "How do checks and balances work? Give one example of how one branch can limit another.",
    "q2_placeholder": "One example of checks and balances is...",
    "q3_text": "Why is the Herald wrong to say the three branches 'just do the same thing'?",
    "q3_placeholder": "The Herald is wrong because...",
    "quiz_q1_text": "Which branch of government has the power to make laws?",
    "quiz_q1_a": "The executive branch (the President)",
    "quiz_q1_b": "The legislative branch (Congress)",
    "quiz_q1_c": "The judicial branch (the courts)",
    "quiz_q2_text": "What is the purpose of checks and balances in the Constitution?",
    "quiz_q2_a": "To make sure all three branches always agree",
    "quiz_q2_b": "To prevent any one branch from becoming too powerful",
    "quiz_q2_c": "To let the President control Congress and the courts",
    "quiz_q3_text": "Why is the Herald's claim that the three branches 'are just three lists of jobs' misleading?",
    "quiz_q3_a": "Because the founders copied the British system exactly",
    "quiz_q3_b": "Because each branch has different powers and can check the others — they were separated on purpose to protect citizens",
    "quiz_q3_c": "Because there are actually four branches of government",
    "quiz_perfect_notes": "Perfect score! You clearly understand how the founders divided power. Next issue, we'll explore the Bill of Rights.",
    "quiz_review_notes": "Let's review. Article I gives Congress the power to make laws. Article II gives the President the power to enforce laws. Article III gives courts the power to interpret laws. Checks and balances keep any one branch from becoming too powerful.",
    "assignment_video_notes": "For your Front Page Brief, use your Editor's Notebook notes. Write 3-5 sentences explaining how the Constitution divides power and why checks and balances matter.",
    "assignment_guidance": "Write a short brief (3–5 sentences) explaining how the Constitution divides power among the three branches. Name at least one check or balance and explain why the founders designed the system this way.",
    "assignment_placeholder": "FRONT PAGE BRIEF — Three Branches of Government\n\nThe Constitution divides power into three branches... Article I gives Congress... Checks and balances work by...",
    "archive_topic": "how the Constitution divides power among the three branches of government",
    "checklist_artifact": "Wrote a headline and front page brief",
    "cert_message": "You reported the truth about the three branches — each with its own power, each with its own limits. That's honest reporting.",
    "next_tease": "A new dispatch arrives at the <em>Editorial Board</em> — and <strong>The Hasty Herald has already rushed to print</strong>. Next issue, the Herald claims citizens have rights with no need for limits. You'll investigate the Bill of Rights and discover what protects freedom. Editors, sharpen your pencils.",
    "closing_notes": "Today you investigated Articles I, II, and III and discovered that the three branches aren't just lists — they're a system of separated powers with checks and balances. Next time, the Editorial Board meets to examine the Bill of Rights.",
    "gathered_artifact_label": "FRONT PAGE BRIEF",
    "gathered_desk": "Front Page Desk",
})

# I'll write a data file for the remaining 9 lessons to keep this manageable
# Actually, let me put them all inline but more compactly

# Lesson data is loaded from a separate file
exec(open("/sessions/awesome-ecstatic-goldberg/mnt/optima-5th-social-studies/build_lessons_data.py").read())


def build_lesson(lesson):
    """Build a lesson HTML from the appropriate base template."""
    L = lesson

    # Select base
    if L["base"] == "fp":
        html = BASE_FP
        old_code = "5.11.01"
        old_code_hyph = "5-11-01"
        old_title = "How and Why the U.S. Government Was Created by the Constitution"
        old_issue = 55
        old_week = 28
        old_circ = "3,920"
        old_artifact = "Front Page Brief"
        old_virtue = "Honesty"
        old_virtue_lc = "honesty"
        old_unit_code = "G5-U11"
        old_unit_title = "Constitution and Constitutional Republic"
        old_standards = "SS.5.CG.1.2; SS.5.CG.1.3; SS.5.CG.1.4; SS.5.CG.2.3; SS.5.CG.2.4; SS.5.CG.2.5; SS.5.CG.3.1; SS.5.CG.3.2; SS.5.CG.3.3; SS.5.CG.3.4; SS.5.CG.3.5; SS.5.CG.3.6; SS.5.HE.1.1"
    elif L["base"] == "eb":
        html = BASE_EB
        old_code = "5.11.02"
        old_code_hyph = "5-11-02"
        old_title = "Representative Government and the Constitutional Republic"
        old_issue = 56
        old_week = 28
        old_circ = "3,940"
        old_artifact = "Editorial Board Recommendation"
        old_virtue = "Honesty"
        old_virtue_lc = "honesty"
        old_unit_code = "G5-U11"
        old_unit_title = "Constitution and Constitutional Republic"
        old_standards = "SS.5.CG.1.2; SS.5.CG.1.3; SS.5.CG.1.4; SS.5.CG.2.3; SS.5.CG.2.4; SS.5.CG.2.5; SS.5.CG.3.1; SS.5.CG.3.2; SS.5.CG.3.3; SS.5.CG.3.4; SS.5.CG.3.5; SS.5.CG.3.6; SS.5.HE.1.1"
    elif L["base"] == "mr":
        html = BASE_SD
        old_code = "5.10.08"
        old_code_hyph = "5-10-08"
        old_title = "Revolutionary War Campaign Map and Timeline"
        old_issue = 54
        old_week = 27
        old_circ = "3,900"
        old_artifact = "Gazette Correction"
        old_virtue = "Courage"
        old_virtue_lc = "courage"
        old_unit_code = "G5-U10"
        old_unit_title = "From Revolution to Republic"
        old_standards = "SS.5.A.5.1; SS.5.A.5.2; SS.5.A.5.3; SS.5.A.5.4; SS.5.A.5.5; SS.5.A.5.6; SS.5.A.5.7; SS.5.AA.1.1"

    # For map room: convert source-desk to map-room
    if L["base"] == "mr":
        html = html.replace("source-desk", "map-room")
        html = html.replace("Source Desk", "Map Room")
        html = html.replace('<div class="desk-icon-wrap">\U0001f50d</div>', '<div class="desk-icon-wrap">\U0001f5fa️</div>')
        html = html.replace('\U0001f50d The Desk', '\U0001f5fa️ The Desk')
        html = html.replace("Continue to \U0001f50d The Desk", "Continue to \U0001f5fa️ The Desk")
        html = html.replace("Where one source is examined for what it says — and leaves out.", "Where map evidence helps explain patterns and choices.")
        old_artifact = "Gazette Correction"  # after conversion still need to swap

    # Global text replacements
    new_circ = f"{L['circ']:,}"
    html = html.replace(old_code, L["code"])
    html = html.replace(old_code_hyph, L["code_hyph"])
    html = html.replace(old_title, L["title"])
    html = html.replace(f"Issue {old_issue}", f"Issue {L['issue']}")
    html = html.replace(f"issue-{old_issue}", f"issue-{L['issue']}")
    html = html.replace(f"Week {old_week}", f"Week {L['week']}")
    html = html.replace(f"~{old_circ}", f"~{new_circ}")

    if old_unit_code != L["unit_code"]:
        html = html.replace(old_unit_code, L["unit_code"])
    if old_unit_title != L["unit_title"]:
        html = html.replace(old_unit_title, L["unit_title"])
    if old_standards != L["standards"]:
        html = html.replace(old_standards, L["standards"])

    # Virtue
    if old_virtue != L["virtue"]:
        html = html.replace(f"★ Editor's Lens · {old_virtue} ★", f"★ Editor's Lens · {L['virtue']} ★")
        html = html.replace(f'<span class="editors-desk-virtue-tag">{old_virtue}</span>', f'<span class="editors-desk-virtue-tag">{L["virtue"]}</span>')

    # ─── NEWSROOM STATUS ───
    html = re.sub(
        r'(Vol\. 1 · Issue \d+ · Circulation ~[\d,]+ · <em>).*?(</em>)',
        lambda m: m.group(1) + _newsroom_summary(L) + m.group(2),
        html, count=1
    )
    html = re.sub(
        r'(<strong>Vol\. 1 · Issue \d+</strong> — <em>).*?(</em>)',
        lambda m: m.group(1) + L["story_phase"] + m.group(2),
        html, count=1
    )
    html = re.sub(
        r'(<span class="circulation-unit">readers</span>\s*</span>\s*\n\s*— ).*?\n',
        lambda m: m.group(1) + _circ_flavor(L) + '\n',
        html, count=1
    )
    html = re.sub(
        r'(<strong>Ms\. Avery</strong> — ).*?\n',
        lambda m: m.group(1) + L["avery_short"] + '\n',
        html, count=1
    )

    # ─── LAST EDITION ───
    # Summary line
    html = re.sub(
        r'(<span class="story-block-label">Last Edition</span>\s*<span class="story-block-summary">\s*\n?\s*).*?(\s*</span>\s*\n\s*<span class="story-block-toggle">)',
        lambda m: m.group(1) + L["last_edition_summary"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )
    # Body
    html = re.sub(
        r'(Last issue\'s Archive Line (?:read: |asked |explained )).*?(?=\s*</div>\s*</div>\s*</div>\s*\n\s*<!-- )',
        lambda m: L["last_edition_archive"],
        html, count=1, flags=re.DOTALL
    )

    # ─── DISPATCH ───
    html = re.sub(
        r'(<div class="dispatch-body">\s*(?:<!--[^>]*-->\s*)*<p>).*?(</p>)',
        lambda m: m.group(1) + L["dispatch"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── BEAT ───
    html = re.sub(
        r'(<div class="intro-card-body">\s*(?:<!--[^>]*-->\s*)*<p>).*?(</p>)',
        lambda m: m.group(1) + L["beat_label"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── OBJECTIVES ───
    obj_pat = r'(<div class="obj-line"><span class="obj-icon">▸</span> ).*?(</div>\s*<div class="obj-line"><span class="obj-icon">▸</span> ).*?(</div>\s*<div class="obj-line"><span class="obj-icon">▸</span> ).*?(</div>)'
    html = re.sub(obj_pat, lambda m: m.group(1) + L["obj1"] + m.group(2) + L["obj2"] + m.group(3) + L["obj3"] + m.group(4), html, count=1, flags=re.DOTALL)

    # ─── NEED STRIP ───
    if L["base"] == "mr":
        html = html.replace('<span class="need-chip">Gazette Correction</span>', f'<span class="need-chip">{L["artifact_label"]}</span>')
    elif L["artifact_label"] != old_artifact:
        html = html.replace(f'<span class="need-chip">{old_artifact}</span>', f'<span class="need-chip">{L["artifact_label"]}</span>')

    # ─── WELCOME VIDEO ───
    html = re.sub(
        r'(<div class="video-placeholder-label">Welcome Video</div>\s*<div class="video-placeholder-title">).*?(</div>)',
        lambda m: m.group(1) + f'Welcome to Issue {L["issue"]}: {L["title"]}' + m.group(2),
        html, count=1, flags=re.DOTALL
    )
    html = re.sub(
        r'(Welcome Video.*?<strong>Teacher recording notes:</strong> ).*?(</div>)',
        lambda m: m.group(1) + L["welcome_notes"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── PATH STEPS ───
    html = re.sub(
        r'(<span class="todays-path-step"><span class="todays-path-step-num">2</span>).*?(</span>)',
        lambda m: m.group(1) + L["path_step2"] + m.group(2),
        html, count=1
    )
    html = re.sub(
        r'(<span class="todays-path-step"><span class="todays-path-step-num">3</span>).*?(</span>)',
        lambda m: m.group(1) + L["path_step3"] + m.group(2),
        html, count=1
    )

    # ─── VIRTUE TEXT ───
    html = re.sub(
        r'(<div class="virtue-lens-text">\s*(?:<!--[^>]*-->\s*)*).*?(\s*</div>\s*</div>\s*\n\s*<!-- HASTY HERALD)',
        lambda m: m.group(1) + L["virtue_text"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── HERALD ───
    html = re.sub(r'(<div class="herald-headline">).*?(</div>)', lambda m: m.group(1) + L["herald_headline"] + m.group(2), html, count=1)
    html = re.sub(r'(<p class="herald-claim">).*?(</p>)', lambda m: m.group(1) + L["herald_claim"] + m.group(2), html, count=1)
    html = re.sub(
        r'(<div class="herald-task">\s*(?:<!--[^>]*-->\s*)*<strong>Your job, junior editor:</strong> ).*?(\s*</div>)',
        lambda m: m.group(1) + L["herald_task"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── ROLE TEXT ───
    desk_name = _desk_for_role(L)
    html = re.sub(
        r'(<div class="role-text">).*?(</div>\s*</div>\s*\n\s*<!-- EDITOR)',
        lambda m: m.group(1) + f'\n      <strong>Your role today:</strong> You are a <strong>Junior Editor</strong> on the <strong>{desk_name}</strong> at The Republic Gazette. {L["role_text"]}\n    ' + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── SOCRATIC ───
    html = re.sub(
        r'(<div class="editors-desk-question">\s*(?:<!--[^>]*-->\s*)*).*?(\s*</div>\s*<div class="editors-desk-prompt">)',
        lambda m: m.group(1) + f'"{L["socratic"]}"' + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── EDITOR'S FOLLOW-UP ───
    html = re.sub(
        r'(<div class="editors-desk-prompt">\s*(?:<!--[^>]*-->\s*)*).*?(\s*</div>\s*</div>\s*</div>\s*\n)',
        lambda m: m.group(1) + L["editors_followup"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── EXPLORE VIDEO ───
    html = re.sub(
        r'(<div class="video-placeholder-label">Explore Video</div>\s*<div class="video-placeholder-title">).*?(</div>)',
        lambda m: m.group(1) + f'At the {desk_name}: {L["title"]}' + m.group(2),
        html, count=1, flags=re.DOTALL
    )
    html = re.sub(
        r'(Explore Video.*?<strong>Teacher recording notes:</strong> ).*?(</div>)',
        lambda m: m.group(1) + L["explore_notes"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── TAB 2 CONTENT ───
    tab2_pattern = r'(<!-- ═══ CONTENT SECTIONS.*?-->\s*)(.*?)(\s*<div class="reflection-block">)'
    html = re.sub(tab2_pattern, lambda m: m.group(1) + L["tab2_content"].strip() + '\n\n  ' + m.group(3), html, count=1, flags=re.DOTALL)

    # ─── NOTEBOOK ───
    html = re.sub(
        r'(<h3>\U0001f4d3 Editor\'s Notebook</h3>\s*<p[^>]*>).*?(</p>)',
        lambda m: m.group(1) + L["notebook_intro"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )
    # Q1-Q3
    for i, qi in enumerate(['q1', 'q2', 'q3'], 1):
        html = re.sub(
            rf'(<span class="reflection-q-num">{i}</span>\s*).*?(\s*<span class="reflection-save-dot")',
            lambda m, qi=qi: m.group(1) + L[f"{qi}_text"] + m.group(2),
            html, count=1, flags=re.DOTALL
        )
        html = re.sub(
            rf'(id="journal-{qi}"[^>]*placeholder=").*?(")',
            lambda m, qi=qi: m.group(1) + L[f"{qi}_placeholder"] + m.group(2),
            html, count=1
        )

    # ─── QUIZ ───
    for i in [1, 2, 3]:
        html = re.sub(
            rf'(<span class="factcheck-q-num">{i}</span>\s*<span class="factcheck-q-text">).*?(</span>)',
            lambda m, i=i: m.group(1) + L[f"quiz_q{i}_text"] + m.group(2),
            html, count=1, flags=re.DOTALL
        )
        html = _replace_quiz_options(html, f'fc-q{i}', L[f"quiz_q{i}_a"], L[f"quiz_q{i}_b"], L[f"quiz_q{i}_c"])

    # ─── QUIZ VIDEOS ───
    html = re.sub(
        r'(Quiz Perfect Video.*?<strong>Teacher recording notes:</strong> ).*?(</div>)',
        lambda m: m.group(1) + L["quiz_perfect_notes"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )
    html = re.sub(
        r'(Quiz Review Video.*?<strong>Teacher recording notes:</strong> ).*?(</div>)',
        lambda m: m.group(1) + L["quiz_review_notes"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── ASSIGNMENT VIDEO ───
    html = re.sub(
        r'(<div class="video-placeholder-title">Writing Your ).*?(</div>)',
        lambda m: m.group(1) + L["artifact_label"] + m.group(2),
        html, count=1
    )
    html = re.sub(
        r'(Assignment Explainer Video.*?<strong>Teacher recording notes:</strong> ).*?(</div>)',
        lambda m: m.group(1) + L["assignment_video_notes"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── ASSIGNMENT ARTIFACT ───
    # Mini masthead artifact label
    if old_artifact != L["artifact_label"]:
        html = html.replace(f'<span>{old_artifact}</span>', f'<span>{L["artifact_label"]}</span>', 1)
    # Article label
    html = re.sub(
        r'(<div class="gazette-article-label">★ ).*?( — Junior Editor\'s Submission ★</div>)',
        lambda m: m.group(1) + L["artifact_label"] + m.group(2),
        html, count=1
    )
    # Guidance
    html = re.sub(
        r'(<strong>What goes in a ).*?(:</strong>\s*\n\s*<span>).*?(</span>)',
        lambda m: m.group(1) + L["artifact_label"] + m.group(2) + L["assignment_guidance"] + m.group(3),
        html, count=1, flags=re.DOTALL
    )
    # Body textarea
    html = re.sub(
        r'(<textarea class="gazette-body-input"[^>]*data-label=").*?("[^>]*placeholder=").*?(")',
        lambda m: m.group(1) + L["artifact_label"] + m.group(2) + L["assignment_placeholder"] + m.group(3),
        html, count=1, flags=re.DOTALL
    )

    # ─── ARCHIVE LINE ───
    html = re.sub(
        r'(write what <strong>future citizens</strong> should remember about ).*?(\.\s*\n)',
        lambda m: m.group(1) + L["archive_topic"] + '.\n',
        html, count=1, flags=re.DOTALL
    )

    # ─── GATHERED ───
    html = re.sub(
        r'(All of your editor\'s notes, ).*?(, and archive line)',
        lambda m: m.group(1) + L["artifact_label"].lower() + m.group(2),
        html, count=1
    )
    html = re.sub(
        r"(lines\.push\('--- )FRONT PAGE BRIEF|EDITORIAL BOARD RECOMMENDATION|GAZETTE CORRECTION( ---'\))",
        lambda m: (m.group(1) or "lines.push('--- ") + L["gathered_artifact_label"] + (m.group(2) or " ---')"),
        html, count=1
    )
    # Fix gathered artifact label more carefully
    for old_ga in ["FRONT PAGE BRIEF", "EDITORIAL BOARD RECOMMENDATION", "GAZETTE CORRECTION"]:
        if f"'--- {old_ga} ---'" in html:
            html = html.replace(f"'--- {old_ga} ---'", f"'--- {L['gathered_artifact_label']} ---'", 1)
            break
    # Gathered desk line
    html = re.sub(
        r"(lines\.push\('  Vol\. 1 · Issue \d+ · ).*?('\))",
        lambda m: m.group(1) + L["gathered_desk"] + m.group(2),
        html, count=1
    )

    # ─── CHECKLIST ───
    html = re.sub(
        r'(<div class="checklist-row" onclick="toggleCheck\(this\)"><div class="checklist-box"></div><span>Wrote a headline and ).*?(</span></div>)',
        lambda m: m.group(1) + L["artifact_label"].lower() + m.group(2),
        html, count=1
    )

    # ─── CERTIFICATE ───
    if L["next_code"]:
        # Regular lesson
        pass
    else:
        # Final lesson
        html = re.sub(r'<div class="cert-headline">Issue \d+ Published</div>',
                      '<div class="cert-headline">Final Edition Published</div>', html, count=1)

    html = re.sub(
        r'(<div class="cert-message">.*?<strong>Well done, Junior Editor\.</strong> ).*?(\s*</div>)',
        lambda m: m.group(1) + L["cert_message"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    # ─── NEXT ISSUE ───
    if L["next_code"]:
        html = re.sub(
            r'(<div class="next-issue-label">★ In the Next Issue \().*?(\) ★</div>)',
            lambda m: m.group(1) + L["next_code"] + m.group(2),
            html, count=1
        )
        html = re.sub(
            r'(<div class="next-issue-title">).*?(</div>)',
            lambda m: m.group(1) + L["next_title"] + m.group(2),
            html, count=1
        )
        html = re.sub(
            r'(<div class="next-issue-tease">\s*(?:<!--[^>]*-->\s*)*).*?(\s*</div>\s*</div>\s*\n\s*<!-- )',
            lambda m: m.group(1) + L["next_tease"] + m.group(2),
            html, count=1, flags=re.DOTALL
        )
    else:
        html = re.sub(
            r'<div class="next-issue-teaser">.*?</div>\s*</div>',
            '<div class="next-issue-teaser">\n    <div class="next-issue-label">★ The Republic Gazette Signs Off ★</div>\n    <div class="next-issue-title">Thank You, Junior Editors</div>\n    <div class="next-issue-tease">\n      This is the final issue of The Republic Gazette. You have investigated with honesty, courage, courtesy, and service. You are an <strong>American Historian-Citizen</strong>. The Gazette is proud of every edition you published. Go serve the common good.\n    </div>\n  </div>',
            html, count=1, flags=re.DOTALL
        )

    # ─── CLOSING VIDEO ───
    html = re.sub(
        r'(<div class="video-placeholder-title">Going to Press · Issue )\d+(</div>)',
        lambda m: m.group(1) + str(L["issue"]) + m.group(2),
        html, count=1
    )
    html = re.sub(
        r'(Closing Video.*?<strong>Teacher recording notes:</strong> ).*?(</div>)',
        lambda m: m.group(1) + L["closing_notes"] + m.group(2),
        html, count=1, flags=re.DOTALL
    )

    return html


def _desk_for_role(L):
    if L["base"] == "fp": return "Front Page Desk"
    elif L["base"] == "eb": return "Editorial Board"
    elif L["base"] == "mr": return "Map Room"

def _newsroom_summary(L):
    if L["code"] == "5.12.01": return "New unit, new questions — the republic begins to expand."
    elif L["code"] == "5.13.01": return "Final unit — time to curate the American Historian-Citizen Exhibition."
    else: return f"Investigating {L['title'].lower()}."

def _circ_flavor(L):
    if L["issue"] <= 58: return "Steady readership. Keep earning their trust with honest reporting."
    elif L["issue"] <= 62: return "Readership climbing. Your courageous reporting is making a difference."
    elif L["issue"] <= 64: return "Almost at full circulation. The community trusts your reporting."
    else: return "Peak circulation. The Gazette has served its readers all year long."

def _replace_quiz_options(html, q_id, opt_a, opt_b, opt_c):
    pattern = rf"(id=\"{q_id}\".*?<div class=\"factcheck-options\">)(.*?)(</div>\s*<div class=\"factcheck-feedback\")"
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        print(f"WARNING: Could not find quiz options for {q_id}")
        return html
    options_block = match.group(2)
    options_block = re.sub(r'(factcheck-option-letter">A</span>\s*<span>).*?(</span>)', lambda m: m.group(1) + opt_a + m.group(2), options_block, count=1, flags=re.DOTALL)
    options_block = re.sub(r'(factcheck-option-letter">B</span>\s*<span>).*?(</span>)', lambda m: m.group(1) + opt_b + m.group(2), options_block, count=1, flags=re.DOTALL)
    options_block = re.sub(r'(factcheck-option-letter">C</span>\s*<span>).*?(</span>)', lambda m: m.group(1) + opt_c + m.group(2), options_block, count=1, flags=re.DOTALL)
    html = html[:match.start(2)] + options_block + html[match.end(2):]
    return html


# BUILD
results = []
for L in LESSONS:
    html = build_lesson(L)
    filename = f"ss-{L['code_hyph']}-{L['kebab']}.html"
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    size = os.path.getsize(filepath)
    pencil_count = html.count('✏️')
    results.append((filename, size, pencil_count))
    print(f"OK {filename} -- {size:,} bytes -- {pencil_count} pencils remaining")

print(f"\nTotal: {len(results)} lessons built")
for fn, sz, pc in results:
    print(f"  {fn}: {sz:,} bytes, {pc} pencils")
