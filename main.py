import argparse
from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FTPTarget
from ftpsync.synchronizers import UploadSynchronizer


def run(args: argparse.Namespace):
    local = FsTarget(args.local_dir)
    remote = FTPTarget(args.remote_dir, args.host, args.port, 
            username=args.user, password=args.passwd)
    dry_run = (args.dry_run == 'True') or (args.dry_run == 'true')
    opts = {'dry_run': dry_run, 'verbose': 4, 'exclude': args.exclude}
    s = UploadSynchronizer(local, remote, opts)
    s.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for FTP Deploy')
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--port', type=int, default=21)
    parser.add_argument('--user', type=str, required=True)
    parser.add_argument('--passwd', type=str, required=True)
    parser.add_argument('--local_dir', type=str, default='./')
    parser.add_argument('--remote_dir', type=str, default='/')
    parser.add_argument('--dry_run', type=str, default='False', choices=('True', 'False', 'true', 'fasle'))
    parser.add_argument('--exclude', type=str, default='.DS_Store,.git')
    args = parser.parse_args()
    # print(f'{args=}')
    run(args)
