Title: Patterns in Chaos
Date: 2014-05-09 12:00
Modified: 2014-05-09 12:00
Slug: patterns-in-chaos
Author: Joonas Haapala
Summary: Patterns in Chaos
Status: draft

In this post I will try to describe and visualize the basic working mechanisms of the Cortical Learning Algorithm (or CLA) by [Numenta](http://numenta.org/) and at the same time explain how [CortiCL](http://github.com/Jontte/CortiCL) implements it. This description is based on the 0.2.1 version (September 2011) of the [HTM CLA whitepaper](http://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf) and at the time of writing there's already some talk on improving these methods in the mailing list.

The algorithm is split into two parts: the spatial pooler and the temporal pooler. 

Spatial pooler
==============

It all begins with a multi-channel stream of bits. The source might be a camera, a temperature sensor or another layer of CLA, the algorithm doesn't care. What's important is that individual channels in the stream are boolean and carry a semantic meaning instead of a raw sensory reading. For example, to convert a temperature to this representation one could have each bit denote whether the temperature is within a certain temperature range. 

{% img center {filename}/images/data_in_1.svg Raw sensory input data %}

At this point we have no control over the sparsity (the number of active bits at a given time) of the data. The main purpose of the spatial pooler is to filter the stream so that we end up with a fixed sparsity stream as required by the temporal pooler.


- KUVA SP COLUMNEISTA


In CLA theory this collection of bits is called a sparse distributed representation (SDR) and you will hear them mention it often

CortiCL demo programs come with a class called 'Sensor' that 


{% img center {filename}/images/data_in_2.svg Raw sensory input data with column activations %}


Temporal pooler
===============



