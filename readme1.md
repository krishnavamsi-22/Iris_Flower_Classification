# SidebarActivities Component

## Overview
The `SidebarActivities` component is a React functional component used in course chapters to display and navigate through activities. It dynamically renders activity information, provides intuitive navigation, and visually represents activity types and statuses.

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

## Workflow and Data Flow

### Fetching Data

1. Extracts `courseId` from route parameters using `useParams`.
2. Fetches activity-related data from the Redux store:
   - `currentActivityId`: The currently selected activity.
   - `activityStates`: Contains data about each activity (e.g., type, title, status).
   - `activityOrder`: Order in which activities are displayed.

---

### User Interaction

| **Action**            | **Handler Function**     | **Effect**                                                                      |
|------------------------|--------------------------|---------------------------------------------------------------------------------|
| Click on Activity      | `handleActivityClick`    | Updates the Redux state with the selected activity and highlights it.           |
| Click Back Button      | `handleBackbutton`       | Navigates to the chapter list and resets the sidebar to its global state.       |

---

### Rendering Activities

- Maps through `activityOrder` to dynamically generate a list of activities.
- Each activity includes:
  - **Icon**: Based on `activity_type`.
  - **Title and Description**: Rendered based on activity type.
  - **Duration**: Indicates estimated time to complete.
- Highlights the currently selected activity.

---

## State Management

### Redux State Updates

| **Action**                     | **State Slice**    | **Effect**                                                                 |
|---------------------------------|--------------------|-----------------------------------------------------------------------------|
| `setCurrentActivity(activityId)`| `session`          | Updates the current activity ID.                                           |
| `setSidebar("global")`          | `global`           | Resets the sidebar state to the global view.                               |

---

### Local State

| **State**        | **Purpose**                                    |
|-------------------|------------------------------------------------|
| `Loading State`   | Controls the display of a spinner during data fetch. |

---

## Component Lifecycle

### useEffect Hook

| **Purpose**               | **Effect**                                                                  |
|----------------------------|-----------------------------------------------------------------------------|
| Fetch initial data         | Ensures required activity data is fetched when the component mounts.        |
| Manage navigation context  | Sets up sidebar and breadcrumb navigation for seamless transitions.         |

---

## Mermaid Diagram

### Workflow

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
