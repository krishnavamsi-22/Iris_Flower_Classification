# SidebarActivities Component

## Overview
The SidebarActivities component is a React functional component used in course chapters to display and navigate through activities. It provides an intuitive UI to help users explore and manage activities with visual indicators and seamless navigation.



## Features
| *Feature*              | *Description*                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| *Dynamic Rendering*     | Fetches and displays activities dynamically based on the current course and chapter. |
| *Activity Icons*        | Uses icons to represent activity types like videos, quizzes, and reading materials. |
| *Navigation*            | Includes a back button to navigate to the chapter list and links to activity details. |
| *State Management*      | Utilizes Redux for global state management.                                      |
| *Loading State*         | Displays a loading spinner while fetching activity data.                        |

---

## Dependencies
| *Hook/Library*    | *Purpose*                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------|
| useNavigate        | Navigate programmatically between routes.                                                   |
| useParams          | Retrieve route parameters like courseId.                                                  |
| useAppDispatch     | Dispatch actions to the Redux store.                                                        |
| useAppSelector     | Select state slices from the Redux store.                                                   |
| react-icons        | Display icons for activity types and statuses.                                              |
| Redux Slices         | session for activity-related data and global for UI state like sidebars.                |

---

## Workflow and Data Flow

### Fetching Data
1. Extract courseId from route parameters.
2. Use Redux selectors to fetch:
   - currentActivityId: Currently selected activity.
   - activityStates: State of all activities including type, title, and status.
   - activityOrder: Order in which activities are displayed.

### User Interaction
| *Action*              | *Handler Function*         | *Effect*                                                                 |
|--------------------------|------------------------------|-----------------------------------------------------------------------------|
| Click on Activity        | handleActivityClick        | Updates Redux with the selected activity and highlights it in the list.    |
| Click Back Button        | handleBackbutton           | Navigates to the chapter list and resets the sidebar to its global state.  |

### Rendering Activities
- Maps through activityOrder to dynamically generate a list of activities.
- Each activity displays:
  - *Icon*: Based on activity_type.
  - *Title and Description*: Conditionally displayed for clarity.
  - *Duration*: Indicates estimated time to complete.

---

## State Management

### Redux State Updates
| *Action*                   | *State Slice*      | *Effect*                                                                 |
|-------------------------------|----------------------|-----------------------------------------------------------------------------|
| setCurrentActivity(activityId) | session           | Updates the current activity ID.                                           |
| setSidebar("global")        | global             | Resets the sidebar state to the global view.                               |

### Local State
- *Loading State*: Manages the display of the spinner while data is fetched.

---

## Component Lifecycle
### useEffect Hook
| *Purpose*          | *Effect*                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------|
| Fetch initial data    | Ensures the component fetches required activity data upon mounting.                        |
| Manage navigation     | Sets up sidebar and breadcrumb context for seamless navigation.                           |

---

## Mermaid Diagram
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


## Workflow and Data Flow

### Sequence Diagram: Component Workflow


sequenceDiagram
    participant User
    participant Component
    participant ReduxStore
    participant Backend

    User->>Component: Load SidebarActivities
    Component->>ReduxStore: Fetch currentActivityId, activityStates, activityOrder
    ReduxStore-->>Component: Provide required activity data
    Component->>Backend: Fetch course-related data (if required)
    Backend-->>Component: Return course data
    Component-->>User: Render activity list and UI

    User->>Component: Click on an Activity
    Component->>ReduxStore: Dispatch setCurrentActivity(action)
    ReduxStore-->>Component: Update currentActivityId

    User->>Component: Click Back Button
    Component->>ReduxStore: Dispatch setSidebar("global")
    Component-->>User: Navigate to Chapters

