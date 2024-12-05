db.getCollection("applications").insert( {
    _id: ObjectId("675167dd34177893b5853fb2"),
    authorized_to_work: "yes",
    city_state: "New York, NY",
    cover_letter_path: "files/20241205164413/Cover Letter2.txt",
    current_residence: "yes",
    email: "john.doe@gmail.com",
    first_name: "John",
    job_id: "675005e6876d8e519f0731e1",
    last_name: "Doe",
    linkedin_profile: "https://linkedin.com/in/johndoe",
    require_visa_sponsorship: "no",
    resume_path: "files/20241205164413/Resume1.txt",
    state: NumberInt("1")
} );
db.getCollection("applications").insert( {
    _id: ObjectId("6751680434177893b5853fb3"),
    authorized_to_work: "yes",
    city_state: "Los Angeles, CA",
    cover_letter_path: "files/20241205164452/Cover Letter2.txt",
    current_residence: "yes",
    email: "jane.smith@gmail.com",
    first_name: "Jane",
    job_id: "675005e6876d8e519f0731e1",
    last_name: "Smith",
    linkedin_profile: "https://\tlinkedin.com/in/janesmith",
    require_visa_sponsorship: "no",
    resume_path: "files/20241205164452/Resume2.txt",
    state: NumberInt("0")
} );
db.getCollection("applications").insert( {
    _id: ObjectId("6751682334177893b5853fb4"),
    authorized_to_work: "yes",
    city_state: "Chicago, IL",
    cover_letter_path: "files/20241205164523/Cover Letter1.txt",
    current_residence: "no",
    email: "alice.johnson@gmail.com",
    first_name: "Alice",
    job_id: "675005e6876d8e519f0731e1",
    last_name: "Johnson",
    linkedin_profile: "https://linkedin.com/in/alicejohn",
    require_visa_sponsorship: "yes",
    resume_path: "files/20241205164523/Resume1.txt",
    state: NumberInt("-1")
} );
db.getCollection("applications").insert( {
    _id: ObjectId("6751684034177893b5853fb5"),
    authorized_to_work: "no",
    city_state: "Houston, TX",
    cover_letter_path: "files/20241205164552/Cover Letter2.txt",
    current_residence: "yes",
    email: "bob.brown@gmail.com",
    first_name: "Bob",
    job_id: "675006c3876d8e519f0731e3",
    last_name: "Brown",
    linkedin_profile: "https://linkedin.com/in/bobbrown",
    require_visa_sponsorship: "no",
    resume_path: "files/20241205164552/Resume2.txt",
    state: NumberInt("0")
} );
db.getCollection("applications").insert( {
    _id: ObjectId("6751687a34177893b5853fb7"),
    authorized_to_work: "yes",
    city_state: "San Francisco, CA",
    cover_letter_path: "files/20241205164650/Cover Letter2.txt",
    current_residence: "yes",
    email: "carol.wilson@gmail.com",
    first_name: "Carol",
    job_id: "675006c3876d8e519f0731e3",
    last_name: "Wilson",
    linkedin_profile: "https://linkedin.com/in/carolw",
    require_visa_sponsorship: "no",
    resume_path: "files/20241205164650/Resume1.txt",
    state: NumberInt("0")
} );
