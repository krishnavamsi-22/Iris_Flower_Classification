# SidebarActivities Component

## Overview
The SidebarActivities component is a React functional component used in course chapters to display and navigate through activities. It provides an intuitive UI to help users explore and manage activities with visual indicators and seamless navigation.

---

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
    A[User Opens SidebarActivities] -->|Fetch Data| B[Fetch Session Data via Redux]
    B -->|Data Loaded| C[Render Activity List]
    C -->|Click on Activity| D[Update Redux State with Selected Activity]
    D -->|Navigate| E[Display Activity Details]
    C -->|Click Back| F[Navigate to Chapters]
    F --> G[Reset Sidebar State]
