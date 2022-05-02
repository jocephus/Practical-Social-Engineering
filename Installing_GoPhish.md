## Setting up GoPhish
GoPhish is an automated phishing utility written in the Go language. In order to use it, you’ll need to have an SMTP server to send the mail through and a web server at which victims will land. Although you can create both of these within GoPhish, doing so might increase your chances of detection. I suggest setting up these three firewall rules to prevent detection or collateral damage:

 - Allow port **3333/tcp** (the port for the GoPhish web admin interface) and port 22 (the SSH port) from your network only
 - Allow port **80/tcp** (the default port for your landing page, though you could use port **443/tcp** with an SSL/TLS certificate for more realism) from your network and the victim IP ranges only
 - Allow port **25/tcp** (the port for SMTP traffic) in the outbound direction only

### GoLang

efore installing GoPhish, you need to install GoLang. Instructions for doing so are located [here](https://github.com/golang/go/wiki/Ubuntu)).

### Installing GoPhish
From the [GoPhish documentation](https://docs.getgophish.com/user-guide/installation), installation is as simple as:

 - To install GoPhish, simply run:
	'go get github.com/gophish/gophish`

- This downloads GoPhish into your `$GOPATH`
 - Next, navigate to:
		`$GOPATH/src/github.com/gophish/gophish` 
 - and run the command:
		`go build`
 - This builds a GoPhish binary in the current directory.
