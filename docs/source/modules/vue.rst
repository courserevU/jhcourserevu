Frontend
#########

- Sign in takes the user to a Google login pop-up
- The user will enter the site at the landing page, where its functionality and purpose is introduced.
- There is a button on that landing page that, if clicked, will take the user to the list of courses they can review. There is also a button on the navigation bar at the top that will take the user to that same course display page. There are links to our GitHub page and docs, and there is a button to take the user to the list of courses they have marked as taken (if not logged in then there are no courses displayed there.)
- The dark mode button on the navigation bar (sun/moon icon) can be clicked to switch between light and dark themes for the site as a whole. This preference is saved in local storage so it persists between sessions.
- There is a search bar for the user to search courses on this course list page. They can search by course name, course number, or department.
- The course display has a pagination selector underneath the list of courses to split up the courses into manageable tile displays of 10 at a time.
- If the user prefers to view the items in vertical list format rather than tile format, there is a toggle button near the search bar.
- From the course list page, for each course tile, you can click a button to write a review or click a button to read reviews for that particular course - each of these buttons will take you to a different page for that purpose. The "Write Review" button is only visible if that courses has been marked "taken" by checking the checkbox on the course tile/list item that says "I have taken this course."
- When the above checkbox is checked, the course will also appear on the My Courses page. If the user wants to remove the course from this "taken" list, they can uncheck the checkbox and the course will no longer appear on the My Courses page.
- The review list page will display all reviews for a course, with a pagination selector underneath to split up the reviews into manageable tile displays of 10 at a time.
- There is a dropdown menu where the user can opt to only display a certain comment category (like exam style or workload.)
- In order to write a review, you will be prompted to enter the name of the professor and answer a series of guided questions about the course. When done, the user can click the submit button to post their review. A toast notification will tell the user if their review was submitted successfully (green), or if there was an error or not all fields are completed (yellow).
- At any point, if the user wants to return to the landing page, they can click the logo to take them back there.
