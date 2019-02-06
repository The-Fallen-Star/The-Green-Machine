def typeDecision(detectedWord):
    # List of common substrings from each category
    # This will be updated to hold other possible outputs
    trash = ["junk", "trash", "chip"]
    recycle = ["plastic", "paper", "can", "glass", "styrafoam"]
    compost = ["food", "snack"]

    # Variables used to return the number that will
    # trigger the corresponding bin
    trashDecision = 0
    recycleDecision = 1
    compostDecision = 2

    # Search the trash list to find a match
    for element in trash:
        if detectedWord.find(element) != -1:
            return trashDecision

    # Search the rescycle list to find a match
    for element in recycle:
        if detectedWord.find(element) != -1:
            return recycleDecision

    # Search the compost list to find a match
    for element in compost:
        if detectedWord.find(element) != -1:
            return compostDecision

    # If nothing is returned thus far, then return
    # the trashDecision by default
    return trashDecision

# Testing input strings
print(typeDecision("potato chips")) # Should return 0
print(typeDecision("paper plate")) # Should return 1
print(typeDecision("leftover food")) # Should return 2
print(typeDecision("null")) # Should return 0
