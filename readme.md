
# SidebarActivities Component

## Overview

The `SidebarActivities` component is a React functional component designed to provide an interactive sidebar for navigating through activities within a course chapter. It utilizes Redux for state management and supports user interactions like activity selection and navigation.



## Workflow

### Component Initialization

1. **Fetch Route Parameters**:
   - Extract `courseId` using `useParams` to determine the course context.
2. **Retrieve Redux State**:
   - Access state using `useAppSelector`:
     - `activityOrder`: Sequence of activities.
     - `currentActivityId`: Currently selected activity.
     - `activityStates`: Status of activities (e.g., completed/in-progress).
3. **Render Activities**:
   - Map over `activityOrder` to display:
     - **Icon**: Represents activity type (e.g., video, quiz).
     - **Title**: Name of the activity.
     - **Status Indicator**: Shows completion or progress.



### User Interactions

1. **Activity Selection**:
   - Clicking an activity triggers `handleActivityClick`:
     - Updates Redux state with `setCurrentActivity(activityId)`.
     - Navigates to the activity details page.
2. **Back Button**:
   - Clicking the back button triggers `handleBackbutton`:
     - Resets sidebar view using `setSidebar("global")`.
     - Navigates back to the chapters list.



## State Management

### Redux State Structure

```typescript
interface AppState {
  session: {
    currentActivityId: number;
    activityStates: {
      [key: number]: {
        activity: ActivityType;
        attempt: AttemptType;
      };
    };
    activityOrder: number[];
  };
}


### State Flow Table

| **State Type**      | **Managed By** | **Purpose**                                              |
|----------------------|----------------|----------------------------------------------------------|
| `currentActivityId`  | Redux          | Highlights the active activity.                         |
| `activityStates`     | Redux          | Tracks progress for each activity.                      |
| `activityOrder`      | Redux          | Determines the rendering order of activities.           |
| Loading Status       | `useSessionData` | Controls the loading spinner during data fetching.     |

### Redux Actions

| **Action**                   | **Redux Slice**    | **Effect**                               |
|-------------------------------|--------------------|------------------------------------------|
| `setCurrentActivity(activityId)` | `session`         | Updates the selected activity in state.  |
| `setSidebar("global")`        | `global`           | Resets the sidebar to the global view.   |



## Activity Rendering

- Each activity is dynamically rendered with:
  - **Icon**: Corresponds to the activity type.
  - **Title**: Displays the activity name.
  - **Completion Status**: Indicates if the activity is completed or in progress.

### Activity Icon Logic


graph TD
    A[Activity Type Input] --> B{Switch Statement}
    B -->|Written Answer| C[MdSlowMotionVideo]
    B -->|Study Material| D[IoBookOutline]
    B -->|Multiple Choice| E[FiEdit]
    B -->|Default| F[FiEdit]



## Component Flowchart

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


## Component Lifecycle Events

| **Phase**      | **Actions**                             | **Dependencies**         |
|-----------------|-----------------------------------------|--------------------------|
| Mount          | Initialize hooks, fetch data            | `useSessionData`         |
| Update         | Re-render activity list                 | `activityOrder`, `activityStates` |
| Interaction    | Handle clicks, update state             | Dispatch, `navigate`     |
| Unmount        | Clean up subscriptions                  | None                     |



## Sequence Diagram for User Interactions

sequenceDiagram
    participant User as User
    participant Component as SidebarActivities
    participant Redux as Redux Store
    participant Router as React Router

    User->>Component: Interact with Activity
    Component->>Redux: Dispatch Action
    Redux-->>Component: Update Redux State
    Component->>Router: Navigate to Details
    Component->>UI: Re-render UI
    UI-->>User: Show Updated State

---

## Data Transformation Pipeline


flowchart LR
    A[Raw Activity Data] -->|Redux Selection| B[Filtered Data]
    B -->|Processing| C[UI Ready Data]
    
    subgraph "Data Transformation"
        C -->|Map Function| D[Activity Items]
        D -->|Icon Selection| E[Final UI Elements]
    end


## Improvements and Optimizations

| **Aspect**             | **Implementation**       | **Purpose**                           |
|-------------------------|--------------------------|---------------------------------------|
| Redux Selectors         | Use `useAppSelector`     | Efficient state access.               |
| Conditional Rendering   | Loading check           | Prevent unnecessary renders.          |
| Memoization             | Icon computation        | Optimize rendering performance.       |
| Key Prop Usage          | List rendering          | Efficient DOM updates.                |
