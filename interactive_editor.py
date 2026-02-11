import cv2

file = input("Enter your image: ")
image = cv2.imread(file)

if image is None:
    print("Image can't be loaded")
else:
    while True:
        print("\n1: Add Rectangle")
        print("2: Add Circle")
        print("3: Add Text")
        print("4: Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cv2.rectangle(image, (50, 50), (250, 200), (0, 0, 255), 3)

        elif choice == 2:
            cv2.circle(image, (150, 250), 100, (255, 0, 0), 5)

        elif choice == 3:
            cv2.putText(image, "This Poetry is best",
                        (100, 300),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2,
                        (235, 0, 205),
                        4)

        elif choice == 4:
            break

        else:
            print("Invalid choice")
            continue

        cv2.imshow("Edited image", image)
        print("Press any key inside image window to continue...")
        print("Window should be visible now.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        save = int(input("Save image? (1 = Yes, 0 = No): "))
        if save == 1:
            cv2.imwrite("edited_image.png", image)
            print("Image saved!")

        
    
        
