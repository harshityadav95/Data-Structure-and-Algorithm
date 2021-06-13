# Naming StyleGuide

#### C and C++\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=19)\]

In [C](https://en.wikipedia.org/wiki/C_%28programming_language%29) and [C++](https://en.wikipedia.org/wiki/C%2B%2B), [keywords](https://en.wikipedia.org/wiki/Keyword_%28computer_programming%29) and [standard library](https://en.wikipedia.org/wiki/Standard_library) identifiers are mostly lowercase. In the [C standard library](https://en.wikipedia.org/wiki/C_standard_library), abbreviated names are the most common \(e.g. `isalnum` for a function testing whether a character is a numeral\), while the [C++ standard library](https://en.wikipedia.org/wiki/C%2B%2B_standard_library) often uses an underscore as a word separator \(e.g. `out_of_range`\). Identifiers representing [macros](https://en.wikipedia.org/wiki/C_preprocessor#Macro_definition_and_expansion) are, by convention, written using only uppercase letters and underscores \(this is related to the convention in many programming languages of using all-upper-case identifiers for constants\). Names containing double underscore or beginning with an underscore and a capital letter are reserved for implementation \([compiler](https://en.wikipedia.org/wiki/Compiler), [standard library](https://en.wikipedia.org/wiki/Standard_library)\) and should not be used \(e.g. `__reserved` or `_Reserved`\).[\[19\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-19)[\[20\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-20) This is superficially similar to [stropping](https://en.wikipedia.org/wiki/Stropping_%28syntax%29), but the semantics differ: the underscores are part of the value of the identifier, rather than being quoting characters \(as is stropping\): the value of `__foo` is `__foo` \(which is reserved\), not `foo` \(but in a different namespace\).

#### C\#\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=20)\]

[C\#](https://en.wikipedia.org/wiki/C_Sharp_%28programming_language%29) naming conventions generally follow the guidelines published by Microsoft for all .NET languages[\[21\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-21) \(see the .NET section, below\), but no conventions are enforced by the C\# compiler.

The Microsoft guidelines recommend the exclusive use of only [PascalCase](https://en.wikipedia.org/wiki/CamelCase) and [camelCase](https://en.wikipedia.org/wiki/CamelCase), with the latter used only for method parameter names and method-local variable names \(including method-local `const` values\). A special exception to PascalCase is made for two-letter acronyms that begin an identifier; in these cases, both letters are capitalized \(for example, `IOStream`\); this is not the case for longer acronyms \(for example, `XmlStream`\). The guidelines further recommend that the name given to an `interface` be PascalCase preceded by the capital letter I, as in `IEnumerable`.

The Microsoft guidelines for naming fields are specific to `static`, `public`, and `protected` fields; fields that are not `static` and that have other accessibility levels \(such as `internal` and `private`\) are explicitly not covered by the guidelines.[\[22\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-22) The most common practice is to use PascalCase for the names of all fields, except for those which are `private` \(and neither `const` nor `static`\), which are given names that use camelCase preceded by a single underscore; for example, `_totalCount`.

Any identifier name may be prefixed by the commercial-at symbol \(@\), without any change in meaning. That is, both `factor` and `@factor` refer to the same object. By convention, this prefix is only used in cases when the identifier would otherwise be either a reserved keyword \(such as `for` and `while`\), which may not be used as an identifier without the prefix, or a contextual keyword \(such as `from` and `where`\), in which cases the prefix is not strictly required \(at least not at its declaration; for example, although the declaration `dynamic dynamic;` is valid, this would typically be seen as `dynamic @dynamic;` to indicate to the reader immediately that the latter is a variable name\).

#### Go\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=21)\]

In [Go](https://en.wikipedia.org/wiki/Go_%28programming_language%29), the convention is to use `MixedCaps` or `mixedCaps` rather than underscores to write multiword names. When referring to structs or functions, the first letter specifies the visibility for external packages. Making the first letter uppercase exports that piece of code, while lowercase makes it only usable within the current scope.[\[23\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-23)

#### Java\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=22)\]

In [Java](https://en.wikipedia.org/wiki/Java_%28programming_language%29), naming conventions for identifiers have been established and suggested by various Java communities such as Sun Microsystems,[\[24\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-SunJavaCodeConv-24) Netscape,[\[25\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-25) AmbySoft,[\[26\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-26) etc. A sample of naming conventions set by Sun Microsystems are listed below, where a name in "[CamelCase](https://en.wikipedia.org/wiki/CamelCase)" is one composed of a number of words joined without spaces, with each word's -- excluding the first word's -- initial letter in capitals – for example "camelCase".

<table>
  <thead>
    <tr>
      <th style="text-align:left">Identifier type</th>
      <th style="text-align:left">Rules for naming</th>
      <th style="text-align:left">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">Classes</td>
      <td style="text-align:left">Class names should be nouns in <code>Upper</code><a href="https://en.wikipedia.org/wiki/CamelCase"><code>CamelCase</code></a>,
        with the first letter of every word capitalised. Use whole words &#x2013;
        avoid acronyms and abbreviations (unless the abbreviation is much more
        widely used than the long form, such as URL or HTML).</td>
      <td style="text-align:left">
        <ul>
          <li><code>class Raster {}</code>
          </li>
          <li><code>class ImageSprite {}</code>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Methods</td>
      <td style="text-align:left">Methods should be verbs in <code>lower</code><a href="https://en.wikipedia.org/wiki/CamelCase"><code>CamelCase</code></a> or
        a multi-word name that begins with a verb in lowercase; that is, with the
        first letter lowercase and the first letters of subsequent words in uppercase.</td>
      <td
      style="text-align:left">
        <ul>
          <li><code>run();</code>
          </li>
          <li><code>runFast();</code>
          </li>
          <li><code>getBackground();</code>
          </li>
        </ul>
        </td>
    </tr>
    <tr>
      <td style="text-align:left">Variables</td>
      <td style="text-align:left">
        <p>Local variables, instance variables, and class variables are also written
          in <code>lower</code><a href="https://en.wikipedia.org/wiki/CamelCase"><code>CamelCase</code></a>.
          Variable names should not start with underscore (<code>_</code>) or dollar
          sign (<code>$</code>) characters, even though both are allowed. This is
          in contrast to other <a href="https://en.wikipedia.org/wiki/Coding_conventions">coding conventions</a> that
          state that underscores should be used to prefix all instance variables.</p>
        <p>Variable names should be short yet meaningful. The choice of a variable
          name should be <a href="https://en.wikipedia.org/wiki/Mnemonic">mnemonic</a> &#x2014;
          that is, designed to indicate to the casual observer the intent of its
          use. One-character variable names should be avoided except for temporary
          &quot;throwaway&quot; variables. Common names for temporary variables are
          i, j, k, m, and n for integers; c, d, and e for characters.</p>
      </td>
      <td style="text-align:left">
        <ul>
          <li><code>int i;</code>
          </li>
          <li><code>char c;</code>
          </li>
          <li><code>float myWidth;</code>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Constants</td>
      <td style="text-align:left">Constants should be written in uppercase characters separated by underscores.
        Constant names may also contain digits if appropriate, but not as the first
        character.</td>
      <td style="text-align:left">
        <ul>
          <li><code>static final int MAX_PARTICIPANTS = 10;</code>
          </li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Java compilers do not enforce these rules, but failing to follow them may result in confusion and erroneous code. For example, `widget.expand()` and `Widget.expand()` imply significantly different behaviours: `widget.expand()` implies an invocation to method `expand()` in an instance named `widget`, whereas `Widget.expand()` implies an invocation to static method `expand()` in class `Widget`.

One widely used Java coding style dictates that [UpperCamelCase](https://en.wikipedia.org/wiki/CamelCase) be used for [classes](https://en.wikipedia.org/wiki/Class_%28computer_science%29) and [lowerCamelCase](https://en.wikipedia.org/wiki/CamelCase) be used for [instances](https://en.wikipedia.org/wiki/Instance_%28computer_science%29) and [methods](https://en.wikipedia.org/wiki/Method_%28computer_science%29).[\[24\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-SunJavaCodeConv-24) Recognising this usage, some [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment), such as [Eclipse](https://en.wikipedia.org/wiki/Eclipse_%28IDE%29), implement shortcuts based on CamelCase. For instance, in Eclipse's [content assist](https://en.wikipedia.org/wiki/Content_assist) feature, typing just the upper-case letters of a CamelCase word will suggest any matching class or method name \(for example, typing "NPE" and activating content assist could suggest `NullPointerException`\).

Initialisms of three or more letters are CamelCase instead of uppercase \(e.g., `parseDbmXmlFromIPAddress` instead of `parseDBMXMLFromIPAddress`\). One may also set the boundary at two or more letters \(e.g. `parseDbmXmlFromIpAddress`\).

#### JavaScript\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=23)\]

The built-in JavaScript libraries use the same naming conventions as Java. Data types and constructor functions use upper camel case \(RegExp, TypeError, XMLHttpRequest, DOMObject\) and methods use lower camel case \(getElementById, getElementsByTagNameNS, createCDATASection\). In order to be consistent most JavaScript developers follow these conventions.[\[27\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-27) See also: [Douglas Crockford's conventions](https://www.crockford.com/code.html)

#### .NET\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=25)\]

[Microsoft .NET](https://en.wikipedia.org/wiki/Microsoft_.NET) recommends [UpperCamelCase](https://en.wikipedia.org/wiki/CamelCase), also known as PascalCase, for most identifiers. \([lowerCamelCase](https://en.wikipedia.org/wiki/CamelCase) is recommended for [parameters](https://en.wikipedia.org/wiki/Parameter_%28computer_science%29) and [variables](https://en.wikipedia.org/wiki/Variable_%28programming%29)\) and is a shared convention for the .NET languages.[\[30\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-30) Microsoft further recommends that no type prefix hints \(also known as [Hungarian notation](https://en.wikipedia.org/wiki/Hungarian_notation)\) are used.[\[31\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-31) Instead of using Hungarian notation it is recommended to end the name with the base class' name; `LoginButton` instead of `BtnLogin`.[\[32\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-32)



#### Python and Ruby\[[edit](https://en.wikipedia.org/w/index.php?title=Naming_convention_%28programming%29&action=edit&section=30)\]

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) and [Ruby](https://en.wikipedia.org/wiki/Ruby_%28programming_language%29) both recommend `UpperCamelCase` for class names, `CAPITALIZED_WITH_UNDERSCORES` for constants, and `lowercase_separated_by_underscores` for other names.

In Python, if a name is intended to be "[private](https://en.wikipedia.org/wiki/Private_member)", it is prefixed by an underscore. Private variables are enforced in Python only by convention. Names can also be suffixed with an underscore to prevent conflict with Python keywords. Prefixing with double underscores changes behaviour in classes with regard to [name mangling](https://en.wikipedia.org/wiki/Name_mangling#Python). Prefixing and suffixing with double underscores are reserved for "magic names" which fulfill special behaviour in Python objects.[\[39\]](https://en.wikipedia.org/wiki/Naming_convention_%28programming%29#cite_note-pep8-39)\*\*\*\*

\*\*\*\*

**Refrence  :**  

* [https://google.github.io/styleguide/](https://google.github.io/styleguide/)



