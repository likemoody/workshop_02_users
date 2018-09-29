import argparse

description = '''Communication app. Please see help: -h'''

def app(description):
    parser = argparse.ArgumentParser(description=description)
    # adding values' containers to parser (global app container)
    parser.add_argument('-u', '--username',
                        metavar='U',
                        type=str,
                        help='username')
    parser.add_argument('-p', '--password',
                        metavar='P',
                        type=str,
                        help='current password (min 8 symbols)')
    parser.add_argument('-n', '--new_password',
                        metavar='N',
                        type=str,
                        help='new password')
    # flags
    parser.add_argument('-l', '--list',
                        help='list of all users',
                        action='store_true')
    parser.add_argument('-d', '--delete',
                        help='delete user',
                        action='store_true')
    parser.add_argument('-e', '--edit',
                        help='edit username',
                        action='store_true')

    args = parser.parse_args()

    u = args.username
    p = args.password
    n = args.new_password
    l = args.list
    d = args.delete
    e = args.edit

    # uncomment to look into args Namespace object o every container
    # print(u, p, n, l, e, d)
    # print(args)

    # appropriate code ahs to be writen instead of print functions
    if u and p and e == False and d == False:
        print(':: Check credentials >> add user or raise error')
    elif u and p and e and n:
        print(':: Check credentials >> change user password to {} or show message'.format(n))
    elif u and p and d:
        print(':: Check credentials >> delete user or show message')
    elif l:
        print(':: Print out the list of users')
    else:
        parser.print_help()

    return None

if __name__ == "__main__":
    app(description)