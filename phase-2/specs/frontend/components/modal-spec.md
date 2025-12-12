# Modal Component Spec

Props:
- open: boolean
- onClose: fn
- title: string (optional)
- children

Behavior:
- backdrop fade in/out
- modal slide-up on open
- close on ESC & backdrop click
- focus trap inside modal
