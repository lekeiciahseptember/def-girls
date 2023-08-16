menu = input(''' Select one of the following options below:
             Maternal Health 
             Sexual Health 
             Reproductive Health 
             Mental Health 
             Physical Health
        ''').lower()

if menu == "maternal health":
    print("Maternal health pertains to the well-being of women throughout pregnancy, delivery, and the postnatal phase. It is crucial that each of these stages constitutes a favorable and nurturing experience, guaranteeing that both mothers and their infants achieve optimal health and overall well-being.")
    maternal_health = input(''' What would you like to know about Maternal Health ? 
                            1. Pregnancy 
                            2. ChildBirth 
                            3. Post-Natal Care 
                            4. Infertility 
                            5. Child Mortality''')
    if input == "1":
        print("Pregnancy is a natural process in which a female's body undergoes significant changes to nurture and develop a baby. During pregnancy, a pregnant person should prioritize regular prenatal care, maintain a balanced diet, stay hydrated, and engage in moderate exercise if approved by a healthcare provider. Avoiding harmful substances like smoking and alcohol is essential. Emotional well-being is crucial, so managing stress and seeking support are encouraged. Ultimately, each pregnancy is unique, and consulting with a qualified healthcare provider is key to ensure the well-being of both the pregnant person and the developing baby.")
    elif input == "2":
        print("Childbirth is the process of delivering a baby from the mother's womb. During childbirth, a pregnant person should follow the advice of healthcare professionals, create a birth plan, and pack essentials for the hospital stay. Staying informed about the stages of labor, pain management options, and potential complications is vital. Having a support person or doula can provide emotional and physical assistance. After childbirth, postpartum care, rest, and seeking help for any health concerns are essential for a healthy recovery.")
    elif input == "3":
        print("Post-natal care is the medical and emotional support provided to a woman after childbirth. It focuses on the mother's well-being, recovery, and newborn care. Key aspects include monitoring physical healing, managing postpartum symptoms, and addressing mental health needs. Seeking help is vital, and new mothers can turn to healthcare providers, family, or support groups for assistance with breastfeeding, baby care, and emotional adjustments. Promptly discussing any concerns or complications with a healthcare professional ensures a smoother postpartum journey and a healthy start for both mother and baby.")
    elif input == "4":
        print("Infertility is the inability to conceive after trying for a year or more. Preventive measures include maintaining a healthy lifestyle, avoiding smoking and excessive alcohol, and managing stress. During infertility, self-care involves seeking support from loved ones and healthcare professionals. Adopting a balanced diet, regular exercise, and stress-reduction techniques can promote emotional well-being. Exploring fertility treatments or assisted reproductive technologies with medical guidance may offer options. Acknowledging emotions, joining support groups, and seeking counseling can help cope with the emotional challenges of infertility.")
    elif input == "5":
        print("Child mortality is the death of children under the age of five. Causes include infectious diseases, malnutrition, and inadequate healthcare. In South Africa, child mortality has decreased but remains a concern, with a mortality rate of about 30 deaths per 1,000 live births. Prevention involves improving healthcare access, vaccination programs, and nutrition. Education on safe motherhood practices and proper child care is crucial. Community-based interventions, early diagnosis, and timely treatment can reduce child mortality rates. Strengthening healthcare systems and addressing social determinants are vital steps toward effectively dealing with child mortality.")
    else:
        print("That is an invalid option, please choose an option available on the list.")    