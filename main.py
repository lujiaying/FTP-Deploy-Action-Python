import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for FTP Deploy')
    parser.add_argument('--arg1', type=str, required=True)
    args = parser.parse_args()
    print(f'{args=}')
