def main(arguments) -> None:
    from modules.DockerHub import DockerHub
    from modules.Banner import Banner
    results = DockerHub.search(arguments.search, arguments.size)
    Banner.print()

    if results['total'] > 0: 
        counter = 1
        for image in results['results']:
            id          = image['id']
            foundedTags = []
            tags = DockerHub.getTags(id, arguments.size)

            for tag in tags['results']:
                foundedTags.append(tag['name'])

            foundedTags = ', '.join(foundedTags)
            createdAt   = image['created_at']
            updatedAt   = image['updated_at']
            print(f'[{counter}] Founded: {Fore.GREEN}{id} {Style.RESET_ALL}(Tags: {foundedTags}){Fore.GREEN} - Created At: {createdAt} - Updated At: {updatedAt} {Style.RESET_ALL}')
            counter = counter + 1

    else:
        print('Nothing was found :/')

if __name__ == '__main__':
    from colorama import init, Fore, Style
    import argparse
    
    parser = argparse.ArgumentParser(description='Hubber - A simple python script to search Docker Images inside a Docker Public Registry.')
    parser.add_argument('--search', action='store', type=str, required=True)
    parser.add_argument('--size', action='store', type=int, required=False, default=25)
    main(parser.parse_args())