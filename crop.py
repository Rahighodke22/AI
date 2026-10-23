# ---------------------------------------------------------
# EXPERT SYSTEM FOR CROP DISEASE DIAGNOSIS
# ---------------------------------------------------------

def get_answer(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def crop_diagnosis():
    print("=" * 55)
    print("        CROP DISEASE DIAGNOSIS EXPERT SYSTEM")
    print("=" * 55)
    print("Answer the following questions with yes or no.\n")

    # Collect symptoms
    yellow_leaves = get_answer("Are the leaves turning yellow?")
    brown_spots = get_answer("Are there brown or dark spots on the leaves?")
    white_powder = get_answer("Is there a white powdery coating on the leaves?")
    fuzzy_mold = get_answer("Is there fuzzy or moldy growth on the leaves/stem?")
    wilting = get_answer("Are the plants wilting?")
    stunted_growth = get_answer("Is the plant growth stunted?")
    leaf_holes = get_answer("Are there holes or chewed edges on the leaves?")
    curled_leaves = get_answer("Are the leaves curling or twisting?")
    insects_visible = get_answer("Can you see insects on the plants?")
    sticky_residue = get_answer("Is there a sticky residue on the leaves?")
    root_rot = get_answer("Are the roots or stem base soft, dark or rotting?")
    dry_edges = get_answer("Are the leaf edges dry or scorched?")
    fruit_spots = get_answer("Are there dark spots or rot on the fruits?")
    wet_conditions = get_answer("Has the weather/soil been very wet or humid recently?")

    print("\n" + "=" * 55)
    print("                 DIAGNOSIS")
    print("=" * 55)

    # -----------------------------------------------------
    # RULES (more specific rules are placed first)
    # -----------------------------------------------------

    # Rule 1: Powdery Mildew
    if white_powder:
        diagnosis = "Powdery Mildew"
        explanation = (
            "A white powdery coating on leaves is the classic sign "
            "of powdery mildew."
        )
        advice = "Improve air flow and apply a suitable sulfur-based or recommended fungicide."

    # Rule 2: Downy Mildew / Mold
    elif fuzzy_mold and yellow_leaves and wet_conditions:
        diagnosis = "Possible Downy Mildew / Fungal Mold"
        explanation = (
            "Fuzzy growth with yellowing leaves in humid or wet "
            "conditions suggests downy mildew."
        )
        advice = "Avoid overhead watering, remove infected leaves and use a recommended fungicide."

    # Rule 3: Root Rot
    elif root_rot and wilting and yellow_leaves:
        diagnosis = "Possible Root Rot"
        explanation = (
            "Rotting roots with wilting and yellow leaves can occur "
            "with root rot, often from waterlogged soil."
        )
        advice = "Improve drainage, reduce watering and remove badly affected plants."

    # Rule 4: Leaf Spot / Blight
    elif brown_spots and yellow_leaves and wet_conditions:
        diagnosis = "Possible Leaf Spot / Blight"
        explanation = (
            "Brown spots with yellowing leaves in wet or humid weather "
            "are commonly linked to fungal or bacterial leaf spot or blight."
        )
        advice = "Remove infected leaves, avoid wetting foliage and rotate crops."

    # Rule 5: Sap-sucking pests
    elif insects_visible and sticky_residue and curled_leaves:
        diagnosis = "Possible Aphid / Whitefly Infestation"
        explanation = (
            "Insects, sticky honeydew and curling leaves are typical "
            "of sap-sucking pests."
        )
        advice = "Use neem oil or insecticidal soap and encourage natural predators."

    # Rule 6: Chewing pests
    elif leaf_holes and insects_visible:
        diagnosis = "Possible Caterpillar / Beetle Damage"
        explanation = (
            "Holes or chewed leaf edges with visible insects point to "
            "chewing pests."
        )
        advice = "Hand-pick pests where possible or use a recommended biological pesticide."

    # Rule 7: Fruit rot
    elif fruit_spots and wet_conditions:
        diagnosis = "Possible Fruit Rot / Anthracnose"
        explanation = (
            "Dark spots or rot on fruits in wet conditions can occur "
            "with fungal fruit diseases."
        )
        advice = "Remove infected fruits, improve spacing and avoid excess moisture."

    # Rule 8: Viral disease
    elif curled_leaves and stunted_growth and yellow_leaves and not insects_visible:
        diagnosis = "Possible Viral Disease"
        explanation = (
            "Leaf curling, yellowing and stunted growth can occur "
            "with plant viruses, which are often spread by pests."
        )
        advice = "Remove and destroy infected plants and control insect carriers."

    # Rule 9: Nutrient deficiency
    elif yellow_leaves and stunted_growth and not brown_spots:
        diagnosis = "Possible Nutrient Deficiency"
        explanation = (
            "Yellow leaves with poor growth and no spots can occur "
            "with nitrogen or other nutrient deficiency."
        )
        advice = "Test the soil and apply suitable fertilizer or compost."

    # Rule 10: Water stress
    elif wilting and dry_edges and not root_rot:
        diagnosis = "Possible Water Stress / Heat Stress"
        explanation = (
            "Wilting with dry or scorched leaf edges and healthy roots "
            "can occur from drought or heat."
        )
        advice = "Water deeply and regularly, and use mulch to retain moisture."

    # No matching rule
    else:
        diagnosis = "No Clear Diagnosis"
        explanation = (
            "The symptoms do not match the rules in this "
            "expert system."
        )
        advice = "Consult a local agriculture officer or extension service."

    print("\nPossible Condition:", diagnosis)
    print("Reason:", explanation)
    print("Suggested Action:", advice)

    # Spread warning
    if root_rot or (wilting and fuzzy_mold):
        print("\nWARNING:")
        print("This condition can spread quickly to nearby plants.")
        print("Isolate or remove affected plants promptly.")

    print("\nNote: This system is for educational purposes only.")
    print("It should not replace advice from a qualified agricultural expert.")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

crop_diagnosis()
