"""Generated using GPT-4"""


# Step 1: Begin the quest with a list of mysteries
def initiate_quest():
    mysteries = ["lost_map", "ancient_treasure", "strange_rune", "hidden_path"]
    findings = []
    print("Embarking on a journey to uncover ancient secrets...")
    return mysteries, findings


# Step 2: Investigate each mystery in the list
def investigate_mystery(mystery):
    print(f"Investigating: {mystery}...")
    if "treasure" in mystery:
        print(f"Success! {mystery} has unveiled a great discovery!")
        return f"Found {mystery}"
    else:
        print(f"{mystery} holds some intrigue, but nothing remarkable.")
        return None


# Step 3: Walk through each mystery and collect notable findings
def explore_mysteries(mysteries):
    _, findings = initiate_quest()
    for mystery in mysteries:
        result = investigate_mystery(mystery)
        if result:
            findings.append(result)
    return findings


# Step 4: Summarize the journey and reveal all findings
def summarize_journey(findings):
    if findings:
        print("\nQuest completed. Our findings include:")
        for finding in findings:
            print(f"- {finding}")
    else:
        print("\nQuest completed. No noteworthy discoveries were made.")


# Launch the exploration
mysteries, _ = initiate_quest()
findings = explore_mysteries(mysteries)
summarize_journey(findings)
