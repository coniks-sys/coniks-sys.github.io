Title: Get Involved
URL: get_involved.html
save_as: get_involved.html
page-order: 4
Summary: Want to get involved with CONIKS? Consider integrating CONIKS into your secure communication service, running an auditor, conducting research, or contributing to our open source software projects.

<div class="col-md-12">
<h4>Integration</h4>
<p>
If you're an engineer or developer for a secure communication service
(small or large), please consider integrating CONIKS into your system
to improve the security and privacy of your users' communications.
This entails running a CONIKS key server for your users and adding support
for the CONIKS protocols in your client software.
</p>
<p>We're happy to help you get started and provide feedback -- feel free
to get in touch!
</p>
</div>

<div class="col-md-12 row-sm">
<h4>Auditors</h4>
<p>
CONIKS's security relies heavily on the number of auditors
checking that CONIKS key servers are not presenting different
clients inconsistent views of the key directories. So the more
auditors there are, the better the chances are of detecting such an
attack. 
</p>
<p>
Whether you've already integrated CONIKS into your service 
or you simply like CONIKS's goals, please consider running a CONIKS auditor. 
This will help grow the network of auditors and ultimately improve 
the security of <em>all</em> CONIKS users.
</p>
<p><b class="text-warning">Note:</b> Unfortunately, we are only now getting 
started with the development of our auditor software package. 
We're currently looking 
for feedback and volunteers to help kickstart this project. Please 
contact us via our mailing list or via email if you're interested in
helping us with the auditor software!</p>
</div>

<div class="col-md-12 row-sm">
<h4>Research</h4>
<p>
If you're a researcher interested in secure messaging, applied cryptography, usable security, and distributed systems, we welcome new collaborations on our <a class="text-success" href="research.html">research</a>, as well as on any new research problems related to CONIKS that may be of interest to you.
</p>
<p>
We have also put together a list of <a class="text-success" href="research.html#openproblems">open
research problems</a> that we learned about as part of design discussions with
engineers working on secure communication tools at major tech companies.
We'd like this list to inform future research in the space of secure messaging, applied
crypto, usable security and distribtued systems. This list is by no means exhaustive, 
so please help us grow this list if you have encountered a new research problem 
we haven't included.
</p>
</div>

<div class="col-md-12 row-sm">
<h4>Open Source Software</h4>
<p>
In our efforts to bring key transparency to all users, we have several
ongoing and planned open source software projects. 
We welcome volunteers, collaborations, and suggestions for new 
features or projects!
Below is a list of projects we're developing and maintaining.
</p>

<div class="inner">
<<<<<<< HEAD
<h5 class="row-sm"><a class="text-info" href="https://github.com/coniks-sys/coniks-java" target="_blank">CONIKS Java library</a></h5>
<p>
The Java library includes basic reference implementations of a
CONIKS server and client to serve as a model for implementing CONIKS. We plan to roll out
a fully functioning standalone CONIKS server in Java in the near future.
</p>
<p>Please see check the <a class="text-success" href="https://github.com/coniks-sys/coniks-java/issues" target="_blank">open issues</a> to see how you can contribute.
</p>

<h5 class="row-sm"><a class="text-info" href="https://github.com/coniks-sys/coniks-go" target="_blank">CONIKS Go library</a></h5>
<p>
The Go library includes the core CONIKS protocol implementation, a Merkle tree implementation, 
a CONIKS crypto implementation, hooks for a C-based client, as well as a fully functioning 
CONIKS key server.
</p>
<p>Please see check the <a class="text-success" href="https://github.com/coniks-sys/coniks-go/issues" target="_blank">open issues</a> to see how you can contribute.
</p>
=======
<h5 class="row-sm"><a class="text-info" href="https://github.com/coniks-sys/coniks-ref-implementation" target="_blank">CONIKS Java reference implementation</a></h5>
<p>
The Java reference implementation is a basic yet fully functional implementation of a
CONIKS server and client. The main goal of this project is
to provide developers of secure communication services with a model for
implementing CONIKS as part of their system. This project may also serve
as a testing ground for researchers looking to design new features or build new
transparency systems.
</p>
<p>Please see the <a class="text-success" href="https://github.com/coniks-sys/coniks-ref-implementation/releases" target="_blank">releases</a> for the current status of this project.
</p>

<h5 class="row-sm"><a class="text-info" href="https://github.com/coniks-sys/libmerkleprefixtree-go" target="_blank">Merkle prefix tree Go library</a></h5>
<p>
The main data structure underlying the CONIKS key directory is a Merkle prefix tree.
This data structure has more general applications as an authenticated, auditable, privacy-preserving key-value store, so this project aims to provide a generic
framework for building applications that may need such a key-value store.
</p>
<p>For now, we are targeting applications written in Golang, including
our new <a class="text-info" href="https://github.com/coniks-sys/libconiks-server-go" target="_blank">CONIKS server Go library</a>. We plan to begin work on a
corresponding Java library in the near future.
</p>
<p><b class="text-warning">Note: This project is in a very early stage. We expect
to have a fully working code base by August 2016.</b>

<h5 class="row-sm"><a class="text-info" href="https://github.com/coniks-sys/libconiks-server-go" target="_blank">CONIKS server Go library</a></h5>
<p>
This CONIKS server library in implements all server-side CONIKS protocols,
providing a framework for developers looking to integrate CONIKS into their
system. This library is built on top of our Merkle prefix tree library.
</p>
<p>For now, we are targeting applications written in Golang, using our <a class="text-info" href="https://github.com/coniks-sys/libmerkleprefixtree-go" target="_blank">Merkle prefix tree Go library</a>. We plan to begin work on a
corresponding server library in Java in the near future.
</p>
<p><b class="text-warning">Note: This project is in a very early stage. We expect
to have a working code base by August 2016.</b>
>>>>>>> 12b74612da8cee39869fe09518ad474168da050f

<h5 class="row-sm">CONIKS Auditor Software Package (Planned)</h5>
<p>
This is a standalone auditor software. The main goal of this project is
to allow any interested parties (communication providers, third parties etc.)
to run an auditor to verify deployed CONIKS key servers.
</p>
</div>
</div>



