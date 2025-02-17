from invoke import task


@task
def test_all(command, browsers="c"):
    browser_map = {"c": "chromium", "ff": "firefox", "w": "webkit"}

    selected_browsers = [browser_map[browser] for browser in browsers.split(",")]

    browser_args = " ".join(f"--browser {browser}" for browser in selected_browsers)
    command.run(f"pytest tests {browser_args} -v", pty=True)


@task
def lint(command):
    command.run("flake8 tests/", pty=True)


@task
def setup(command):
    """Установка зависимостей"""
    command.run("pip install -r requirements.txt", pty=True)
