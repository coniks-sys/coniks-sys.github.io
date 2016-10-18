Title: About CONIKS
URL: about.html
save_as: about.html
page-order: 2
Summary: Trust establishment and key verification are the main challenges to usable end-to-end encrypted communication. CONIKS solves this problem by providing key transparency.

<div class="col-md-12">
<ul>
<li><a href="#whyweneedconiks">Why we need CONIKS</a></li>
<li><a href="#solution">Our Solution</a></li>
</ul>

<hr>

<a name="whyweneedconiks"></a>
<h4>Why we need CONIKS</h4>
<p>Billions of users today rely on online services for their sensitive communication. As these users learn about the myriad of threats to the security and privacy of their communication, their demand for end-to-end secure communication is growing steadily. To meet this demand, an increasing number of existing and new communication service providers are adopting end-to-end encryption. They have realized by now that key management is difficult for the vast majority of users but one important problem remains largely unsolved, namely how do users establish trust? </p>

<p>Trust establishment is about how communicating parties learn about and verify each other’s encryption keys before establishing the secure communication channel. Existing methods for trust establishment have two main problems. Many secure messaging applications require users to establish trust out of band, which is an error-prone and unintuitive process since users must reason explicitly about encryption. Other secure communication services handle key management and trust establishment automatically on behalf of their users, but this allows the service providers (and malicious outsiders!) to tamper with their users' keys giving them access to private messages. CONIKS addresses these shortcomings to create a secure and usable trust establishment method that secure communication service providers can easily adopt.</p>

<a name="solution"></a>
<h4 class="row-md">Our solution: Key Transparency</h4>
<p>CONIKS enables automated trust establishment with untrusted communication service providers by having the service provider maintain an auditable directory of all of its users' keys.</p>

<p>The CONIKS client software on a user's device simply registers the user's online name (e.g. alice@example.com) mapped to a previously-generated public key in the provider's key directory. Then when Alice wants to send a secure message to some other user, say Bob, her CONIKS client looks up Bob's key at the key directory, and verifies that this key has not changed unexpectedly over time. It also checks that this key is consistent with the key other clients are seeing for Bob. Only if these two consistency checks pass will the CONIKS client send Alice's message to Bob. The CONIKS client also performs these same checks for Alice's own key on a regular basis to ensure that the service provider is not tampering with Alice's key.</p>

<p>CONIKS makes these consistency checks possible by requiring that a service provider's key directory be stored in a tamper-evident fashion so that any changes to the contents of the directory are immediately detectable by CONIKS clients. To make these checks efficient, the provider must periodically generate a "summary" of its key directory so clients do not have to check the contents of the directory directly as well as to preserve users' privacy. Lastly, providers must digitally sign these directory summaries as a commitment to the state of their key directory at some point in time, and they must share these summaries with other CONIKS service providers. This way, CONIKS clients can see and compare their view of the provider's key directory with what others in the system are observing, and if a client ever detects inconsistent summaries, clients have irrefutable proof of the misbehavior since they contain the provider's signature.</p>

</div>