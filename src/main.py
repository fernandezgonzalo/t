import argparse
from tabulate import tabulate
from models import Task


def parse_arguments():
    parser = argparse.ArgumentParser(description='sarasa')
    subparsers = parser.add_subparsers(dest="command", help="commands")

    list_parser = subparsers.add_parser('l', help='List tasks')

    add_parser = subparsers.add_parser('a', help='Add tasks')
    add_parser.add_argument('desc', nargs='+')
    add_parser.add_argument('-p', type=int, default=0)

    edit_parser = subparsers.add_parser('e', help='Edit tasks')
    edit_parser.add_argument('id', type=int)
    edit_parser.add_argument('desc', nargs='+')

    remove_parser = subparsers.add_parser('r', help='Remove tasks')
    remove_parser.add_argument('id', type=int)

    return parser.parse_args()


def list_task():
    tasks = [[task.id, task.priority, task.desc] for task in Task]
    headers = ['ID', 'Prior', 'Descripcion']
    print(tabulate(tasks, headers))


def edit_task(task_id, desc):
    try:
        t = Task().get(Task.id == task_id)
        t.desc = desc
        t.save()
    except Task.DoesNotExist:
        print("Task id doesnt exist")


def add_task(desc, priority=0):
    t = Task()
    t.desc = desc
    t.priority = priority
    t.save()


def remove_task(task_id):
    try:
        t = Task().get(Task.id == task_id)
        t.delete_instance()
    except Task.DoesNotExist:
        print("Task id doesnt exist")


def parse_desc(list_words):
    return ' '.join(list_words)


if __name__ == '__main__':
    arguments = parse_arguments()
    print(arguments)

    if arguments.command == 'a':
        add_task(parse_desc(arguments.desc), arguments.p)
    elif arguments.command == 'e':
        edit_task(arguments.id, parse_desc(arguments.desc))
    elif arguments.command == 'l' or arguments.command is None:
        list_task()
    elif arguments.command == 'r':
        remove_task(arguments.id)
