Title: Ray Tracing
Date: 2013-12-16 10:00
Slug: ray-tracing
Author: Joonas Haapala
Summary: Ray Tracing

Ray tracing is one of those cool technologies that pop into my head about once a year. Not only are the results beautiful, it also lets the common geek show his competence at programming to the normal folk. I was hugely inspired by [PixelMachine by SuperJer](http://superjer.com/pixelmachine). His work taught me ray tracing sure isn’t rocket science and you can get astonishing results relatively easily.

### Version 1

If I recall correctly I wrote my first raytracer in 2008. The engine was a bare proof-of-concept and purely based on triangles decorated with some very crude lighting and naive shadows. The scene was either described inline in the source code or by reading external Wavefront .obj files.

The first version, however, lacked a lot in features. I did implement reflective surfaces and alpha transparency, but it wasn’t that interesting as all the surfaces were planar. It was also written in a single threaded way – no way I could benefit from multi-core processors!

[![ray-v1/test_1174936344.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174936344.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174936344.bmp.jpg)
[![ray-v1/test_1174936558.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174936558.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174936558.bmp.jpg)
[![ray-v1/test_1174936674.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174936674.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174936674.bmp.jpg)
[![ray-v1/test_1174938010.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174938010.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174938010.bmp.jpg)
[![ray-v1/test_1174938046.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174938046.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174938046.bmp.jpg)
[![ray-v1/test_1174938170.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174938170.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174938170.bmp.jpg)
[![ray-v1/test_1174940603.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174940603.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174940603.bmp.jpg)
[![ray-v1/test_1174943262.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174943262.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174943262.bmp.jpg)
[![ray-v1/test_1174988444.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test_1174988444.bmp.jpg)]({filename}/images/gallery/ray-v1/test_1174988444.bmp.jpg)
[![ray-v1/test2.bmp.jpg]({filename}/images/gallery/thumbs/ray-v1/test2.bmp.jpg)]({filename}/images/gallery/ray-v1/test2.bmp.jpg)

### Version 2: CSG

This time I took a different approach. The scene was loaded from an XML document that described the scene at hand using constructive solid geometry (CSG), where compex shapes are defined as unions, intersections and complements of primitive shapes. V2 also featured a proper multi-threading model.

V2 was based on photon tracing so rendering consisted of two phases. In phase one we would randomly shoot a predefined amount (usually between 100k and 2 billion) of photons from all sources of light and let them reflect back and forth until the photon was 100% absorbed. For each surface reflection in phase two this ‘lighting map’ was used to calculate the illuminance.

I took advise from [an article in Wikipedia](https://en.wikipedia.org/wiki/Photon_mapping). For spatial lookup of the photons I used a humongous kd-tree using [a very nice C++ implementation](http://libkdtree.alioth.debian.org/) I found.

[![ray-v2/renderer2.png]({filename}/images/gallery/thumbs/ray-v2/renderer2.png)]({filename}/images/gallery/ray-v2/renderer2.png)
[![ray-v2/renderer3.png]({filename}/images/gallery/thumbs/ray-v2/renderer3.png)]({filename}/images/gallery/ray-v2/renderer3.png)
[![ray-v2/renderer4.png]({filename}/images/gallery/thumbs/ray-v2/renderer4.png)]({filename}/images/gallery/ray-v2/renderer4.png)
[![ray-v2/renderer5.png]({filename}/images/gallery/thumbs/ray-v2/renderer5.png)]({filename}/images/gallery/ray-v2/renderer5.png)
[![ray-v2/renderer6.png]({filename}/images/gallery/thumbs/ray-v2/renderer6.png)]({filename}/images/gallery/ray-v2/renderer6.png)
[![ray-v2/renderer7.png]({filename}/images/gallery/thumbs/ray-v2/renderer7.png)]({filename}/images/gallery/ray-v2/renderer7.png)
[![ray-v2/renderer8.png]({filename}/images/gallery/thumbs/ray-v2/renderer8.png)]({filename}/images/gallery/ray-v2/renderer8.png)
[![ray-v2/renderer9.png]({filename}/images/gallery/thumbs/ray-v2/renderer9.png)]({filename}/images/gallery/ray-v2/renderer9.png)
[![ray-v2/renderer10.png]({filename}/images/gallery/thumbs/ray-v2/renderer10.png)]({filename}/images/gallery/ray-v2/renderer10.png)
[![ray-v2/renderer11.png]({filename}/images/gallery/thumbs/ray-v2/renderer11.png)]({filename}/images/gallery/ray-v2/renderer11.png)
[![ray-v2/renderer12.png]({filename}/images/gallery/thumbs/ray-v2/renderer12.png)]({filename}/images/gallery/ray-v2/renderer12.png)
[![ray-v2/renderer13.png]({filename}/images/gallery/thumbs/ray-v2/renderer13.png)]({filename}/images/gallery/ray-v2/renderer13.png)
[![ray-v2/renderer14.png]({filename}/images/gallery/thumbs/ray-v2/renderer14.png)]({filename}/images/gallery/ray-v2/renderer14.png)
[![ray-v2/renderer15.png]({filename}/images/gallery/thumbs/ray-v2/renderer15.png)]({filename}/images/gallery/ray-v2/renderer15.png)
[![ray-v2/renderer17.png]({filename}/images/gallery/thumbs/ray-v2/renderer17.png)]({filename}/images/gallery/ray-v2/renderer17.png)
[![ray-v2/renderer19.png]({filename}/images/gallery/thumbs/ray-v2/renderer19.png)]({filename}/images/gallery/ray-v2/renderer19.png)
[![ray-v2/renderer20.png]({filename}/images/gallery/thumbs/ray-v2/renderer20.png)]({filename}/images/gallery/ray-v2/renderer20.png)
[![ray-v2/renderer22.png]({filename}/images/gallery/thumbs/ray-v2/renderer22.png)]({filename}/images/gallery/ray-v2/renderer22.png)
[![ray-v2/renderer24.png]({filename}/images/gallery/thumbs/ray-v2/renderer24.png)]({filename}/images/gallery/ray-v2/renderer24.png)

### Version 3: Monte Carlo

Aren’t there any ultra-high-realism algorithms that I could use to waste all this processing power?

Path tracing. Photo-grade realism with a simple to understand algorithm.

The idea in nutshell is to shoot rays from the camera and let them bounce randomly in the scene until the ray escapes the scene or hits a light. This makes especially indoor scenes extremely slow to render as the ray might bounce thousands of times before reaching a light.

I also introduced a new surface parameter called roughness. Its a value between 0 and 1 describing the reflective properties of the surface. If roughness is 1, ray is let to bounce in random directions. If its 0, the surface is a perfect mirror. Other values linearly blend between these two extremes. Roughness is best illustrated in the last picture where it changes from 0 on the left to 1 on the right.

Its the slowest algorithm there is, but it approximates the rendering equation pretty nicely.

This time I embedded Google’s powerful V8 JavaScript engine and described the scene in JS. I could programmatically preprocess the scene with simple JavaScript operations such as

`scene.push({type: 'sphere', position: [1,2,3], radius: 1});`

[![ray-v3/rt1.png]({filename}/images/gallery/thumbs/ray-v3/rt1.png)]({filename}/images/gallery/ray-v3/rt1.png)
[![ray-v3/rt2.png]({filename}/images/gallery/thumbs/ray-v3/rt2.png)]({filename}/images/gallery/ray-v3/rt2.png)
[![ray-v3/rt3.png]({filename}/images/gallery/thumbs/ray-v3/rt3.png)]({filename}/images/gallery/ray-v3/rt3.png)
[![ray-v3/rt4.png]({filename}/images/gallery/thumbs/ray-v3/rt4.png)]({filename}/images/gallery/ray-v3/rt4.png)
[![ray-v3/rt5.png]({filename}/images/gallery/thumbs/ray-v3/rt5.png)]({filename}/images/gallery/ray-v3/rt5.png)
[![ray-v3/rt6.png]({filename}/images/gallery/thumbs/ray-v3/rt6.png)]({filename}/images/gallery/ray-v3/rt6.png)
[![ray-v3/rt7.png]({filename}/images/gallery/thumbs/ray-v3/rt7.png)]({filename}/images/gallery/ray-v3/rt7.png)
[![ray-v3/rt8.png]({filename}/images/gallery/thumbs/ray-v3/rt8.png)]({filename}/images/gallery/ray-v3/rt8.png)
[![ray-v3/rt9.png]({filename}/images/gallery/thumbs/ray-v3/rt9.png)]({filename}/images/gallery/ray-v3/rt9.png)
[![ray-v3/rt10.png]({filename}/images/gallery/thumbs/ray-v3/rt10.png)]({filename}/images/gallery/ray-v3/rt10.png)
[![ray-v3/rt11.png]({filename}/images/gallery/thumbs/ray-v3/rt11.png)]({filename}/images/gallery/ray-v3/rt11.png)
[![ray-v3/rt12.png]({filename}/images/gallery/thumbs/ray-v3/rt12.png)]({filename}/images/gallery/ray-v3/rt12.png)
[![ray-v3/rt13.png]({filename}/images/gallery/thumbs/ray-v3/rt13.png)]({filename}/images/gallery/ray-v3/rt13.png)
[![ray-v3/rt14.png]({filename}/images/gallery/thumbs/ray-v3/rt14.png)]({filename}/images/gallery/ray-v3/rt14.png)
[![ray-v3/rt15.png]({filename}/images/gallery/thumbs/ray-v3/rt15.png)]({filename}/images/gallery/ray-v3/rt15.png)
[![ray-v3/rt16.png]({filename}/images/gallery/thumbs/ray-v3/rt16.png)]({filename}/images/gallery/ray-v3/rt16.png)
[![ray-v3/rt17.png]({filename}/images/gallery/thumbs/ray-v3/rt17.png)]({filename}/images/gallery/ray-v3/rt17.png)
[![ray-v3/rt18.png]({filename}/images/gallery/thumbs/ray-v3/rt18.png)]({filename}/images/gallery/ray-v3/rt18.png)
