# Stormy
Basic Bits

## Getting Started

This is a repository of my weird tests.

### Prerequisites

What things you need to install the software and how to install them

```
PHPStorm
XAMPP
GIT
```

### Installing

Generate SSH in GIT

```
sh-keygen -t rsa -b 4096 -C "your_email@example.com"
Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):[Press enter]
Enter passphrase
```
Adding your SSH key to the ssh-agent

Ensure the ssh-agent is running
```
eval $(ssh-agent -s)
```
Add your SSH private key to the ssh-agent.
```
ssh-add ~/.ssh/id_rsa
```
Copy the SSH key to your clipboard
```
clip < ~/.ssh/id_rsa.pub
Github > Setting > SSH
```

## Deployment

```
* [Apache]
* [ PHP ]
```

## Built With

* [Wine]
* [Tears]

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Mae Abigail Banquil** - *Software Engineer* - [Exordium](https://www.behance.net/maebanquil72d7)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

