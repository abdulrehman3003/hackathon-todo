# Button Component Spec

Props:
- children | label
- variant: primary | secondary | ghost | danger
- disabled: boolean
- loading: boolean
- onClick

Behavior:
- When loading, show spinner replacing label
- Primary: filled with --primary
- Hover: transform scale(1.02)
- Transition: transform 160ms, box-shadow 160ms
