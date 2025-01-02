# SidebarActivities Component

## Overview

The SidebarActivities component is a React functional component that provides an interactive sidebar for navigating through activities within a course chapter. It integrates with Redux for state management and handles user interactions like selecting and navigating activities.



## Explanation of Workflow

### Initialization

1. *Fetch Route Parameters*:
   - The courseId is extracted from the URL using the useParams hook.
   - This parameter determines the current course context for fetching activities.

2. *Retrieve Redux State*:
   - The component uses useAppSelector to fetch data from Redux:
     - activityOrder: An array determining the sequence of activities.
     - currentActivityId: The ID of the currently selected activity.
     - activityStates: Information about the status (e.g., completed/in-progress) of each activity.

3. *Render Activities*:
   - Maps over activityOrder to dynamically render the list of activities:
     - Each activity is displayed with:
       - *Icon*: Represents activity type (e.g., video, quiz).
       - *Title*: Name of the activity.
       - *Status Indicator*: Shows if the activity is completed or in progress.

---

### User Interactions

1. *Activity Selection*:
   - Clicking an activity triggers handleActivityClick:
     - Updates the currentActivity in the Redux session slice using setCurrentActivity(activityId).
     - Navigates to the activity details page using useNavigate.

2. *Back Button*:
   - Clicking the back button triggers handleBackbutton:
     - Resets the sidebar state to the global view using setSidebar("global").
     - Navigates back to the chapters list using useNavigate.

---

### State Management

| *State Type*       | *Managed By* | *Purpose*                                                                 |
|-----------------------|----------------|-----------------------------------------------------------------------------|
| *Global State*      | Redux          | Stores activity data (activityOrder, currentActivityId, activityStates). |
| *Local State*       | Component      | Controls UI elements like loading indicators and active item styles.         |

#### Redux Slice Updates

| *Action*                   | *Redux Slice*    | *Effect*                                                                 |
|-------------------------------|--------------------|-----------------------------------------------------------------------------|
| setCurrentActivity(activityId) | session         | Updates the selected activity ID in Redux.                                |
| setSidebar("global")        | global           | Resets the sidebar view to the global state.                              |

---

### Activity Rendering

- Each activity is rendered with:
  - *Icon*: Represents the type of the activity (e.g., video, quiz).
  - *Title*: Name of the activity.
  - *Completion Status*: Indicates whether the activity is completed or in progress.

### Navigation Logic

1. When an activity is clicked:
   - The selected activity ID is updated in Redux.
   - The user is navigated to the activity details page.

2. When the back button is clicked:
   - The sidebar state is reset to the global view.
   - The user is navigated back to the chapter list.

---

## Component Flowchart

```mermaid
graph TD
    A[Component Mounts] --> B[Fetch Route Params]
    B --> C[Retrieve Redux State]
    C --> D[Render Activity List]
    D -->|User Clicks Activity| E[Invoke handleActivityClick]
    E --> F[Update Redux State]
    F --> G[Navigate to Activity Details]
    D -->|User Clicks Back| H[Invoke handleBackbutton]
    H --> I[Reset Sidebar State]
    I --> J[Navigate to Chapters]
