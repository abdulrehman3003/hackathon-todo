# Input Component Spec

Props:
- label
- value
- placeholder
- type: text|email|password|textarea
- error: string
- onChange

Behavior:
- Show label above input
- Show error text under input when error present
- Password type shows toggle button to view/hide password
- Focus outline uses --primary
