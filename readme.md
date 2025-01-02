# SidebarActivities Component

## Overview

The `SidebarActivities` component is a React functional component designed to provide an interactive sidebar for navigating through activities within a course chapter. It utilizes Redux for state management and supports user interactions like activity selection and navigation.

---

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

---

### User Interactions

1. **Activity Selection**:
   - Clicking an activity triggers `handleActivityClick`:
     - Updates Redux state with `setCurrentActivity(activityId)`.
     - Navigates to the activity details page.
2. **Back Button**:
   - Clicking the back button triggers `handleBackbutton`:
     - Resets sidebar view using `setSidebar("global")`.
     - Navigates back to the chapters list.

---

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
