# News Mirror

This project aims to provide an independent news mirror for everyone. Not everyone knows how to install a VPN server
to access news websites and as some news websites are blocked in certain areas in the world. By spinning up this
application on as many machines as possible, the more we can unite and see the full picture of what news outlets
are publishing and draw independent conclusions. We should not create a central place on which we collect all servers 
which are running this application as this will make it easy for countries to ban the news mirror application.

Please help our mission to share the news of the world with everyone!

## How to deploy?

Run the following code to start the News Mirror application:

```bash
docker-compose up --build
```

The News Mirror will then become available at [http://localhost](http://localhost). If you want to change the port, 
feel free to modify to `docker-compose.yaml` file.

## Todo

- [ ] Implement a proxy from independent countries in order to be able to access all news sources around the globe
- [ ] Add more news sources
- [ ] Better display of news on the front page