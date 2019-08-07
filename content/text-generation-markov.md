Title: Fun with Markov chains
Date: 2014-01-22 20:20
Modified: 2014-01-22 22:00
Slug: fun-with-markov-chains
Author: Joonas Haapala
Summary: Text generation using Markov chains
Status: draft

I learnt that it's possible to use Markov chains for primitive text generation.

Markov chains are a useful tool with many applications. A Markov chain is a set of states with the Markov property: the transition probability to the next state only depends on the current state.

Now if I take a piece of text and give each word a unique state I can approximate the probability of jumping from one word to the next by counting the number of jumps in the source text. Next I pick a starting word and start traversing the chain with a [PRNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) at hand.

But what I end up with doesn't sound very much like English. The problem is that languages contain structure and sentences are not just random words crammed in together. By the time the generator jumps to the next word it has already forgotten what it said earlier in the same sentence!

What we can do is give each word triplet one state and call it a third-order Markov chain. Now all transitions depend on the previous three words. This way the system captures common structural primitives in languages and the output start to sound a bit more natural (but it's still pretty far).

I found three to be a pretty good size for word context. Higher order models end up with an exact copy of the source text, unless the source is really, really long.

[Here's some output from my piece of software](http://haapa.la/crusoe.txt). This time my source was Daniel Defoe's Robinson Crusoe.

Here's some generated from [King James's Bible](http://haapa.la/biebl.txt).

Some gems:
> You are to be burned for a sweet smell, an offering of the fruit of the blood at the top of the earth.

> without doubt Joseph has come to the children of Israel, I AM WHAT I AM WHAT I AM WHAT I AM WHAT I AM and he gave him an account of anything


Further reading: [http://www.codinghorror.com/blog/2008/06/markov-and-you.html](http://www.codinghorror.com/blog/2008/06/markov-and-you.html)
