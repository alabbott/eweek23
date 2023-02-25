You're a bored software developer looking to optimize how your day is scheduled. Your day is separated into "events", fixed blocks of time, and "tasks", movable blocks of time with varying priorities.

Your input and output are JSON values matching the following TypeScript notation:

```typescript
type Event = {
    name: string,
    /// Start time in seconds
    start: number,
    /// Length in seconds
    length: number
};

type Task = {
    name: string,
    /// The higher this number is, the sooner it should be scheduled
    priority: number,
    /// Length in seconds
    length: number
};

type Input = {
    events: Event[],
    tasks: Task[]
};

/// Sorted by start time
type Output = Event[];
```

Write a "scheduler" that creates events for those tasks and intersperses them into the list of events that were already scheduled for the day. You can split up a single task into multiple events, but for consistency's sake keep the event names the same as the task name. Your output should be a minified JSON string matching the structure described above. Be careful what order the different properties are listed in!
