from prompts import search_prompts

def main():
    # Example searches
    print("\nSearching for prompts containing 'test':")
    test_prompts = search_prompts("test")
    for prompt in test_prompts:
        print(f"\nID: {prompt.id}")
        print(f"Name: {prompt.name}")
        print(f"Role: {prompt.role}")
        print(f"Description: {prompt.description}")

    print("\nSearching for prompts containing 'care':")
    care_prompts = search_prompts("care")
    for prompt in care_prompts:
        print(f"\nID: {prompt.id}")
        print(f"Name: {prompt.name}")
        print(f"Role: {prompt.role}")
        print(f"Description: {prompt.description}")


if __name__ == "__main__":
    main()
