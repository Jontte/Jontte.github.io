Title: Towards AGI
Date: 2014-05-09 12:00
Modified: 2014-04-02 21:00
Slug: towards-agi
Author: Joonas Haapala
Summary: Towards AGI
Tags:

Mainstream machine learning research focuses on problems with well-defined boundaries. We might be interested in classifying the contents of a photo to a number of buckets: cats, dogs, people, buildings, etc. Or we might want to [predict the number of days a person has to spend in a hospital next year given their medical records](http://www.heritagehealthprize.com/c/hhp).

The Google ImageNet excels at classifying pictures by their contents, but it can't use that knowledge to describe the features it expects a cat to have or draw one when given a robotic arm and a pencil. It does one thing and it does it well which also applies to the Jeopardy!-winning Watson and the Deep Blue supercomputer that famously beat Garry Kasparov in chess.

{% img border {filename}/images/wafflebot.jpg Wafflebot %}

AGI
===

AGI or Artificial General Intelligence is a system that is able to continuously learn from its environment and apply the knowledge in new problem areas. I will argue that in order to construct such a system we will have to pay closer attention to how biology does it.

The methods used in machine learning are often backed by mathematical formulations. For example the backpropagation algorithm for feedforward neural networks is in essence gradient descent of an error function that measures the distance between the desired output and the current output of a complex nonlinear transform. It is a supervised learning algorithm meaning that there exists a third party teacher entity that supplies it pairs of inputs and outputs in the form a training set. This is in contrast to biology where no central 'teacher signal' exists and layers of neurons instead use unsupervised learning to find representations that capture the most information.

In feedforward neural networks information is coded as the average firing rate of a neuron, a real number. In biology, however, rate coding is just one of the [neural coding schemes](https://en.wikipedia.org/wiki/Neural_coding#Coding_schemes) present.


Numenta
=======

[Numenta](http://numenta.org/) is a company that develops a computational model of the neocortex. Their work is mostly open source with a rapidly growing community and I can highly recommend subscribing to their mailing list(s) for interesting and informative discussion about machine intelligence.

I've been following their work for some time now and one of my hobby projects is porting the CLA (Cortical Learning Algorithm) to work on a GPU device via OpenCL. My work is available in GitHub: [http://github.com/Jontte/CortiCL](http://github.com/Jontte/CortiCL). I will describe it in detail in a follow-up blog post.
