# SidebarActivities Component

## Overview
The `SidebarActivities` component is a React functional component used to display and navigate through activities in course chapters. It dynamically renders activity data, facilitates seamless navigation, and visually represents the status of activities using intuitive UI elements.

---

## Features

| **Feature**             | **Description**                                                                |
|--------------------------|--------------------------------------------------------------------------------|
| **Dynamic Rendering**    | Fetches and displays activities dynamically based on the current course/chapter. |
| **Activity Icons**       | Icons represent activity types like videos, quizzes, and reading materials.    |
| **Navigation**           | Includes a back button to navigate to the chapter list and links to activities.|
| **State Management**     | Utilizes Redux for global and session-specific state management.               |
| **Loading State**        | Displays a loading spinner while fetching activity data.                       |

---

## Dependencies

| **Hook/Library** | **Purpose**                                                                          |
|-------------------|--------------------------------------------------------------------------------------|
| `useNavigate`     | Navigate programmatically between routes.                                           |
| `useParams`       | Retrieve route parameters like `courseId`.                                          |
| `useAppDispatch`  | Dispatch actions to the Redux store.                                                |
| `useAppSelector`  | Select state slices from the Redux store.                                           |
| `react-icons`     | Display icons for activity types and statuses.                                      |
| `Redux Slices`    | Manage session-specific activity data and global UI states.                        |
| `Loading`         | Custom component to indicate loading states.                                        |

---

## Component Lifecycle

### Flowchart: Rendering Activities

```mermaid
graph TD
    A[Component Mounts] --> B[Fetch Route Params]
    B --> C[Retrieve Redux State]
    C --> D{Status Check}
    D -->|Success| E[Render Activity List]
    D -->|Not Success| F[Display Loading Spinner]
    E --> G{Activity Clicked?}
    G -->|Yes| H[Dispatch setCurrentActivity]
    G -->|No| I[Wait for Interaction]
    E --> J{Back Button Clicked?}
    J -->|Yes| K[Navigate to Chapters and Dispatch setSidebar]
    J -->|No| L[Stay on Current View]
```

---

### Component States and Effects

- **States**:
  - `currentActivityId`: Tracks the currently active activity.
  - `activityStates`: Represents the completion or progress state of each activity.
  - `activityOrder`: Determines the sequence in which activities are displayed.

- **Effects**:
  - `useEffect`: Fetches activity data whenever the `courseId` or state dependencies change.
  - `useEffect`: Updates the Redux state when the user interacts with the component, such as clicking an activity or the back button.

These states and effects are crucial for maintaining the component's reactivity and ensuring that the UI is always synchronized with the data.

---

### Sequence Diagram: Component Workflow

```mermaid
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
```
