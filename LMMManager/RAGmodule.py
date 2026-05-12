newPrompts = { "en" : """ Please rewrite the following sentence to make it easier 
to understand by non-native with the following 10 simplification rules: "
1.Use short sentences 
2. Choose common, everyday words
3. Avoid idioms, slang, and cultural references
4. Use active voice
5. Repeat key words instead of using synonyms
6. Be concrete and specific
7. Explain or remove abbreviations and acronyms
8. Keep grammar simple. Avoid complex tenses, conditionals, and nested clauses when possible.
9. Use clear structure and formatting
10. Check for clarity, not style
11. Please keep the original language of the text
Please reply only with the simplified sentence. Text to simplify: """,
                "es" : """Por favor, reescribe la siguiente oración para que sea más fácil de entender para personas no nativas, siguiendo las siguientes 10 reglas de simplificación:
1. Usa oraciones cortas.
2. Elija palabras comunes y cotidianas.
3. Evita usar expresiones, jerga y referencias culturales.
4. Usa la voz activa.
5. Repita palabras en lugar de usar sinónimos.
6. Sea concreto y específico.
7. Explica o elimina abreviaturas y acrónimos.
8. Mantenga una gramática gramática simple. Evita usar tiempos verbales complejos, condicionales y las oraciones anidadas siempre que sea posible.
9. Use una estructura y un formato claros.
10. Verifiqca la claridad, no el estilo.
Responda solo con la oración simplificada. Texto para simplificar: """,
                "cat" : """Si us plau, torneu a escriure la frase següent per facilitar-ne la comprensió per a persones no natives amb les 10 regles de simplificació següents: "
1. Utilitzeu frases curtes
2. Trieu paraules comunes i quotidianes
3. Eviteu idiomes, argot i referències culturals
4. Utilitzeu la veu activa
5. Repetiu les paraules en lloc d'utilitzar sinònims
6. Sigueu concrets i específics
7. Expliqueu o elimineu abreviatures i acrònims
8. Manteniu la gramàtica simple. Eviteu els temps verbals complexos, els condicionals i les oracions imbricades sempre que sigui possible.
9. Utilitzeu una estructura i un format clars
10. Comproveu la claredat, no l'estil
Si us plau, responeu només amb la frase simplificada. Text per simplificar: """,
                "it" : """Si us plau, torneu a escriure la frase següent per facilitar-ne la comprensió per a persones no natives amb les 10 regles de simplificació següents: "
1. Utilitzeu frases curtes
2. Trieu paraules comunes i quotidianes
3. Eviteu idiomes, argot i referències culturals
4. Utilitzeu la veu activa
5. Repetiu les paraules en lloc d'utilitzar sinònims
6. Sigueu concrets i específics
7. Expliqueu o elimineu abreviatures i acrònims
8. Manteniu la gramàtica simple. Eviteu els temps verbals complexos, els condicionals i les oracions imbricades sempre que sigui possible.
9. Utilitzeu una estructura i un format clars
10. Comproveu la claredat, no l'estil
Si us plau, responeu només amb la frase simplificada. Text per simplificar: """,
                "ar" : """يرجى إعادة كتابة الجملة التالية بصياغة أبسط، بحيث تكون أسهل فهمًا لغير الناطقين بالعربية المعاصرة، مع الالتزام
بقواعد التبسيط العشر الآتية:
1. استخدم جملًا قصيرة.
2. اختر كلمات شائعة وسهلة من الحياة اليومية.
3. تجنّب التعابير الاصطلاحية، والكلمات العامية، والإشارات الثقافية.
4. استخدم المبني للمعلوم.
5. استخدم الكلمات الأساسية نفسها أكثر من مرة بدلًا من التنويع بالمرادفات.
6. كن واضحًا واذكر الأمور بشكل محدد.
7. اشرح الاختصارات، أو احذفها إذا لم تكن ضرورية.
8. استخدم قواعد وتراكيب بسيطة، وتجنّب الأزمنة المعقدة، وأسلوب الشرط، والجمل المتداخلة قدر الإمكان.
9. استخدم بنية واضحة وترتيبًا سهلًا.
10. اجعل هدفك الوضوح، لا الأسلوب.
يرجى الرد بالجملة المبسطة فقط.
النص المطلوب تبسيطه:""",
                "de" : """ Bitte formulieren Sie den folgenden Satz so um, dass er für Nicht-Muttersprachler leichter verständlich ist. Beachten Sie dabei die folgenden 10 Vereinfachungsregeln:
1. Verwenden Sie kurze Sätze.
2. Wählen Sie gebräuchliche, alltägliche Wörter.
3. Vermeiden Sie Redewendungen, Slang und kulturelle Anspielungen.
4. Verwenden Sie den Aktiv.
5. Wiederholen Sie Schlüsselwörter anstatt Synonyme zu verwenden.
6. Seien Sie konkret und präzise.
7. Erklären oder entfernen Sie Abkürzungen und Akronyme.
8. Halten Sie die Grammatik einfach. Vermeiden Sie nach Möglichkeit komplexe Zeitformen, Konditionalsätze und verschachtelte Nebensätze.
9. Achten Sie auf eine klare Struktur und Formatierung.
10. Prüfen Sie die Verständlichkeit, nicht den Stil.
Bitte antworten Sie nur mit dem vereinfachten Satz. Zu vereinfachender Text: """,
                "gr" : """Παρακαλώ ξαναγράψτε την ακόλουθη πρόταση για να την κατανοήσετε ευκολότερα από μη γηγενείς, με τους ακόλουθους 10 κανόνες απλοποίησης: "
1. Χρησιμοποιήστε σύντομες προτάσεις
2. Επιλέξτε κοινές, καθημερινές λέξεις
3. Αποφύγετε ιδιωματισμούς, αργκό και πολιτισμικές αναφορές
4. Χρησιμοποιήστε ενεργητική φωνή
5. Επαναλάβετε λέξεις-κλειδιά αντί να χρησιμοποιείτε συνώνυμα
6. Να είστε συγκεκριμένοι και συγκεκριμένοι
7. Εξηγήστε ή αφαιρέστε συντομογραφίες και ακρωνύμια
8. Διατηρήστε τη γραμματική απλή. Αποφύγετε σύνθετους χρόνους, υποθετικές υποθέσεις και ένθετες προτάσεις, όταν είναι δυνατόν.
9. Χρησιμοποιήστε σαφή δομή και μορφοποίηση
10. Ελέγξτε για σαφήνεια, όχι για ύφος
Παρακαλώ απαντήστε μόνο με την απλοποιημένη πρόταση. Κείμενο προς απλοποίηση:""",
                "fr" : """Veuillez réécrire la phrase suivante pour la rendre plus compréhensible par les non-anglophones en appliquant les 10 règles de simplification suivantes :
1. Utilisez des phrases courtes.
2. Choisissez un vocabulaire courant.
3. Évitez les expressions idiomatiques, l’argot et les références culturelles.
4. Utilisez la voix active.
5. Répétez les mots clés au lieu d’utiliser des synonymes.
6. Soyez concret et précis.
7. Expliquez ou supprimez les abréviations et les acronymes.
8. Simplifiez votre grammaire. Évitez autant que possible les temps complexes, les conditionnelles et les propositions subordonnées.
9. Utilisez une structure et une mise en forme claires.
10. Privilégiez la clarté au style.
Veuillez répondre uniquement avec la phrase simplifiée. Texte à simplifier :""",
                "prs" : """لطفاً جمله ذیل را با عبارات ساده تر دوباره بنویسید تا درک آن برای گویندگان غیربومی زبان عربی معیاری مدرن آسان تر گردد، در حالیکه به ده قاعده ساده سازی ذیل پایبند باشید:
1. از جملات کوتاه استفاده کنید.
2. کلمات معمول و آسان را از زندگی روزمره انتخاب کنید.
3. از عبارات اصطلاحی، عامیانه، و ارجاعات کلتوری اجتناب کنید.
4. از صدای فعال استفاده کنید.
5. به عوض مترادف های متفاوت از کلمات کلیدی مشابه بیشتر از یک بار استفاده کنید.
6. واضح و مشخص باشید.
7. مخفف ها را توضیح دهید، یا در صورت غیرضروری آنها را حذف کنید.
8. از گرامر و نحو ساده استفاده کنید، و تا حدی ممکن از زمان های پیچیده، جملات مشروط، و جملات همپوشانی اجتناب کنید.
9. از ساختار واضح و سازماندهی آسان استفاده کنید.
10. روی وضوح تمرکز کنید، نه ستایل.
لطفاً فقط با نسخه ساده شده پاسخ دهید.
متن که باید ساده گردد:"""
              }

def GenerateSimplifierPrompt (textToTranslate: str = "", language: str = "en"):
    prompt = newPrompts.get(language, newPrompts["en"]) + textToTranslate + "' "
    prompt = newPrompts[language] + textToTranslate + "' "
    return prompt