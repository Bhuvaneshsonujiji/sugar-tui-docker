
### ✅ main.py
```python
from textual.app import App
from textual.widgets import Static

class DockerTUI(App):
    def compose(self):
        yield Static("Docker Containers:\n- nginx (running)")

if __name__ == '__main__':
    DockerTUI().run()
