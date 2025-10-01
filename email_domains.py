emails = ["alice@gmail.com","bob@yahoo.com","carol@company.org","dave@school.edu","eve123@service.net"]
domains = []
for email in emails:
    domain = (email.split("@")[1])
    domains.append(domain)
print(domains)
