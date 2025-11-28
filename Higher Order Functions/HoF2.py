def email_builder(domain:str):
    def build_email(username:str)->str:
        return f"{username}@{domain}"
    return build_email


if __name__=="__main__":
    gmail=email_builder("gmail.com")
    yahoo=email_builder("yahoo.com")

    print(gmail("yuvha"))
    print(yahoo("dheenakrishna2020"))