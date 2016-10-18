Title: Research
URL: research.html
save_as: research.html
page-order: 3
Summary: Our research on CONIKS seeks to find the most effective and usable way to combine the strong security of manual key verification and the convenience of centralized key servers. Many research problems remain unsolved, which we hope to spur new research ideas.

<div class="col-md-12">
<p>Our research on CONIKS began in an attempt to design a secure webmail service run by an untrusted provider. 
After some time, we realized that the underlying problem in designing a secure webmail service is that the existing 
key management and verification systems have two main drawbacks: managing and verifying key fingerprints manually
is an error-prone process and impractical to automate; centralized service provider-run key servers require that
users blindly trust the provider not to tamper with its users' keys.
We <a class="text-success" href="about.html">designed</a> CONIKS to address these two issues, and we found that the key transparency model was the most suitable
key management and verification model for secure communication services of all kinds.
</p>
<p>We hope that our research will guide the deployment of CONIKS or key transparency systems in existing and
new end-to-end secure communication services, but we also believe that our research may have applications in areas other than
secure communication. At the same time, many problems specific to secure messaging remain unsolved. We have outlined
several of these <a class="text-success" href="#openproblems">open problems</a> that we have encountered so far.</p>
<p>
If you're a researcher interested in secure messaging, we encourage you to consider tackling one of these open problems, 
or to contribute to our list so that others may learn about problems we may not have encountered yet. 
Please feel free to email us or to start a discussion on our mailing list.
</p>

</div>

<div class="col-md-12 row-md">
<h4>Publications</h4>
<div class="col-md-1">
2016
</div>

<div class="col-offset-1 col-md-11">
<p><b>Why Making Johnny's Key Management Transparent is So Challenging</b><br/>
Marcela Melara<br/>
<em>Freedom to Tinker</em><br/>
[<a href="https://freedom-to-tinker.com/blog/masomel/why-making-johnnys-key-management-transparent-is-so-challenging/" target="_blank" class="text-info">blog post</a>]
</p>

<p><b>EthIKS: Using Ethereum to audit a CONIKS key transparency log</b><br/>
Joseph Bonneau<br/>
<em>BITCOIN '16</em><br/>
[<a href="http://www.jbonneau.com/doc/B16b-BITCOIN-ethiks.pdf" target="_blank" class="text-info">paper</a>]
</p>
</div>

<div class="col-md-1 row-sm">
2015
</div>

<div class="col-offset-1 col-md-11 row-sm">
<p><b>CONIKS: Bringing Key Transparency to End Users</b><br/>
Marcela S. Melara, Aaron Blankstein, Joseph Bonneau, Edward W. Felten, Michael J. Freedman<br/>
<em>USENIX Security '15</em><br/>
[<a href="https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-melara.pdf" target="_blank" class="text-info">paper</a>] [<a href="https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/melara" target="_blank" class="text-info">presentation</a>]
</p>

<p><b>Coniks 2.0: Publicly Verifiable Keystore with Key Changing and Verifying Capabilities</b><br/>
Michael Rochlin<br/>
<em>Princeton University</em><br/>
[<a href="static/Rochlin_Michael.pdf" target="_blank" class="text-info">report</a>]
</p>

<p><b>Bringing Deployable Key Transparency to End Users</b><br/>
Marcela S. Melara, Aaron Blankstein, Joseph Bonneau, Edward W. Felten, Michael J. Freedman<br/>
<em>Cryptology ePrint Archive</em><br/>
[<a href="http://eprint.iacr.org/eprint-bin/getfile.pl?entry=2014/1004&version=20150331:044014&file=1004.pdf" target="_blank" class="text-info">draft</a>]
</p>
</div>

<div class="col-md-1 row-sm">
2014
</div>

<div class="col-offset-1 col-md-11 row-sm">
<p><b>CONIKS: Preserving Secure Communication with Untrusted Identity Providers</b><br/>
Marcela S. Melara<br/>
<em>Princeton University</em><br/>
[<a href="https://www.cs.princeton.edu/~melara/static/pubs/mse-thesis.pdf" target="_blank" class="text-info">Master's thesis</a>]
</p>
</div>

</div>

<div class="col-md-12 row-md">
<a name="openproblems"></a>
<h4>Open Research Problems</h4>
CONIKS has provided the first steps towards key transparency and is changing
how communication service providers are thinking about key management.
However, several open challenges that pose major barriers to making CONIKS
truly practical for deployment remain. We identified some of these problems through
discussions with major communication service providers, and summarize these
findings in a <a class="text-info" href="https://freedom-to-tinker.com/blog/masomel/why-making-johnnys-key-management-transparent-is-so-challenging/">blog
post</a>.

<div class="inner">
<h5 class="row-sm"><b>Detecting the source of an inconsistency</b></h5>
<p>
Auditors have
no way of determining whether an inconsistency they detect was introduced
by an outside
attacker who compromised the key server, a system error, or a malicious employee.
Currently, the only party that can be held accountable for an inconsistency
is the identity provider. But identity providers don't want to lose the trust of their users
because of a single malicious employee or because of an outside compromise.
A high-assurance key server would minimize server bugs by using formal verification
and secure hardware, but how can identity providers unambiguously prove that
changes to the directory were made by a single malicious employee or caused by
outside compromise?
</p>

<h5 class="row-sm"><b>Recovering from unintended inconsistencies</b></h5>
<p>
This problem is coupled with a CONIKS server's ability to detect the source of an
inconsistency. Being able to prove the cause of an unintended inconsistency
can help providers maintain their users'  trust, but providers and users also
need to return their system to a stable state after such an inconsistency has occurred.
</p>

<h5 class="row-sm"><b>Secure account recovery after key loss</b></h5>
<p>
Unlike passwords, which may be recovered when lost, there is no way to recover
data encrypted for a lost key, which means a user would lose access to her account.
A more user-friendly approach to account recovery, which is the current default in
CONIKS, is to allow unauthorized key changes. However, this mechanism
undermines users’ security since it doesn’t leave cryptographic evidence and
other clients have no way of distinguishing account recovery from a
compromised account. Therefore, it is crucial to develop a secure account
recovery mechanism, in which it’s unambiguously clear who initiated the recovery.
While key loss is also a problem in other applications such as Bitcoin wallets,
we haven’t explored whether the solutions in those domains could apply to CONIKS.
</p>

<h5 class="row-sm"><b>Detecting false positives</b></h5>
<p>
False positives will cause a CONIKS client to issue warnings prompting the user
about a possible attack. For example, the client will detect an unexpected key
if the user adds a new device or re-installs the app to recover a lost account,
as well as when the key server maliciously changes the user’s key without proper
authorization. Similarly, a warning will be issued for inconsistent directory
summaries, but these may stem from time synchronization problems between
the server and the client, or from an attempt by a malicious key server to
equivocate. It is crucial for the client to be able to distinguish
between the innocuous causes for warnings and the attacks.
</p>

<h5 class="row-sm"><b>Effective user warnings</b></h5>
<p>
This problem is coupled with a CONIKS client's ability to detect false positives.
Users are notorious for ignoring security warnings, so malicious CONIKS key
servers may get away with attacks. Even if CONIKS clients have a mechanism
for detecting false positives, how do we design a user interface that conveys
clearly to users when it’s important for their security to take action on a warning?
</p>

<h5 class="row-sm"><b>Proactive attack prevention</b></h5>
<p>
By design, CONIKS detects attacks after-the-fact as inconsistencies
are only detected once inconsistent signed tree roots have been published.
While the detection guarantees are strong,
they do leave an open window for attack, which depends on the frequency with
which providers publish new STRs. Even though providers are required to publish
temporary bindings whenever a client changes a key directory entry, these only
serve as a non-repudiable promise by the provider to incorporate the changes in
the following epoch. They don't prevent equivocation. Therefore, it is
important to find a practical
solution that is proactive and can mitigate the risks of key server compromise,
instead of relying solely on a reactive system such as CONIKS.
</p>

</div>
</div>
