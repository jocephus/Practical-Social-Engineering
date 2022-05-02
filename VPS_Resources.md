## VPS Resources
### [Digital Ocean](https://m.do.co/c/ab5f75969c8a) (Affiliate Code for $100 credit)

DigitalOcean is a low-cost VPS provider that is mostly cool with security activities and research. They allowed me to run a honeynet of over 20 machines (called Droplets) without batting an eye. 

The pricing model for DigitalOcean is simple. Droplets are billed by the hour, whether the machine is turned off or on. The only way billing does not occur is if the droplet is destroyed. Droplets start at $5 per month. You can add additional storage, backups, managed databases, and optimized servers (memory and CPU) for additional monthly fees. DigitalOcean also supports Kubernetes clusters starting at $10 per node per month. 

**DigitalOcean does not offer professional services.**

You can choose from a variety of Linux flavors such as:

<ul><li>Ubuntu</li><li>Fedora</li><li>CentOS</li><li>Debian</li><li>CoreOS</li><li>FreeBSD</li><li>FedoraAtomic</li><li>RancherOS</li></ul>

There is also a marketplace for prebuilt systems located [here](https://cloud.digitalocean.com/marketplace?i=b366a1)

---
### Linode

Linode is a low-cost VPS provider that competes with DigitalOcean. Instead of Droplets, they refer to VPS instances as Nodes. 

The pricing model for Linode is near identical to DigitalOcean. Nodes are billed by the hour, whether the node is turned off or on. The only way billing does not occur is if the node is destroyed. The nodes start at $5 per month. You can add additional storage, backups, managed databases, and optimized servers (memory and CPU) for additional monthly fees. Although currently in Beta, Linode also plans to support Kubernetes clusters. 

You can choose from a variety of Linux flavors such as:


<ul><li>Ubuntu</li><li>Fedora</li><li>CentOS</li><li>Debian</li><li>CoreOS</li><li>Gentoo</li><li>OpenSuSe</li></ul>


**Linode does offer professional services.**

Although not as robust as DigitalOcean, Linode also has a marketplace for prebuilt systems. Linode has a Beginner's Guide Available [here](https://www.linode.com/docs/platform/billing-and-support/linode-beginners-guide/)

> ***Anything below this line is considered commercial. I do not have experience phishing from these services and in the absence of being able to provide your statement of work (SOW), you may find yourself in legal hot water and/or banned from the platform. Consider this when deciding to use such a platform, especially over a long period of time.***

---
### [Amazon Web Services (AWS)](https://aws.amazon.com/getting-started/)

Amazon offers a very wide array of services. I will admit that the pricing model is not entirely clear. At the surface, there is a free tier that is limited to Linux (Amazon Linux) or Windows for 750 hours. Aside from this, it seems as if the cheapest EC2 (Elastic Computing Cloud) instance is around $18 per month.

**AWS does offer professional services.**

You can choose from a variety of operating systems such as:

<ul><li>Linux (Amazon Linux)</li><li>Red Hat Enterprise Linux (RHEL)</li><li>SuSe Linux Enterprise Server (SLES)</li><li>Windows</li></ul>

Linux and Windows can be configured as standalone or with one of the following three configurations:


<ul><li>with SQL Standard</li><li>with SQL Web</li><li>with SQL Enterprise</li></ul>

Setting up AWS for the first time is outlined [here](https://docs.aws.amazon.com/ec2/?id=docs_gateway)

---
### [Microsoft Azure](https://azure.microsoft.com/en-us/)

Of all the vendor websites that I looked through for this guide, Microsoft's was the least user-friendly. It was challenging to find clearcut pricing and the terminology made it hard to find a plain VPS. As one would expect Microsoft's Azure offers Windows. In addition to Windows, Azure also offers a proprietary Microsoft Linux build. Pricing seems to start around $4.75 per month.

Azure has several ready to go applications that can be installed with a single click, but most of them are overkill for what this guide is designed for.

---
### [Google Cloud Platform (GCP)](https://cloud.google.com/compute)

Google's cloud solution, GCP, seems to be on parity with the other vendors. Pricing is a little higher but more straightforward than Microsoft's. The starting price for a low-end host with no other bells or whistles is $7.30 per month. GCP supports Windows and Linux VPS instances.
