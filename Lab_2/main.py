from View.view import View


def main():
    view = View()
    view.loadEnvironment()
    view.a_star_search(0, 4, 19, 19)