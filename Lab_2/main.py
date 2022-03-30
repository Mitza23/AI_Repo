from View.view import View


def main():
    view = View()
    view.loadEnvironment()
    view.greedy_search(0, 4, 19, 19)
    view.run()