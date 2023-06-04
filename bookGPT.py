import openai

class bookGPT :
    #책 감상을 출력하는 클래스


    @staticmethod
    def arrange(prev_message):
        #문장을 더 자연스럽게 해주는 스크립트

         #gpt에게 넘겨줄 스크립트
        message = "이 문장을 자연스럽게 다듬어줘 : " + prev_message

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content



    #감상 출력 메서드
    @staticmethod
    def review(title,author):
         #gpt에게 넘겨줄 스크립트
        message = "작가 " + author + "의 책 " + title + "의 감상문을 작성해줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content

    #감상 출력 메서드 + 글자수 제한
    @staticmethod
    def review_len(title,author,length):
         #gpt에게 넘겨줄 스크립트
        message = "작가 " + author + "의 책 " + title + "의 감상문을작성해줘"

        message = message + ", 그리고 글자수는 " + length + " 로 작성해줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content

    #책 문장 인용 메서드
    @staticmethod
    def quote(title,author):
        #스크립트
        message = "작가 " + author + "의 책 " + title +  "에서 주요 문장 하나를 인용하고 인용한 이유를 알려줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(

        model ="gpt-3.5-turbo",
        messages=[
            {"role" : "user", "content" : message}
        ]
        )
        #gpt의 답변 반환
        return completion.choices[0].message.content


    #책 문장 인용 메서드 + 글자수 제한
    @staticmethod
    def quote_len(title,author,length):
        #스크립트
        message = "작가 " + author + "의 책 " + title +  "에서 주요 문장 하나를 인용하고 인용한 이유를 알려줘"

        message = message + ", 그리고 글자수는 " + length + " 로 작성해줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(

        model ="gpt-3.5-turbo",
        messages=[
            {"role" : "user", "content" : message}
        ]
        )
        #gpt의 답변 반환
        return completion.choices[0].message.content


    #책 내용 요약 메서드
    @staticmethod
    def summary(title,author):
        #스크립트
        message = "책 " + title + "의 작가는 "+ author + "이고 이 책의 내용을 요약해줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content
    

     #책 내용 요약 메서드 + 글자수 제한
    @staticmethod
    def summary_len(title,author,length):
        #스크립트
        message = "책 " + title + "의 작가는 "+ author + "이고 이 책의 내용을 요약해줘"

        message = message + ", 그리고 글자수는 " + length + " 로 작성해줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content
    
    #토론 주제 및 의견 메서드
    @staticmethod
    def debate(title,author):
        #스크립트
        message = "책 " + title + "의 작가는 "+ author + " 이고 이 책에서 구절 하나를 인용해서 토론 주제를 정하고, 그 주제에 대해서 너의 의견을 말해줘"

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content
    
     #토론 주제 및 의견 메서드 + 글자수 제한
    @staticmethod
    def debate_len(title,author, length):
        #스크립트
        message = "책 " + title + "의 작가는 "+ author + " 이고 이 책에서 구절 하나를 인용해서 토론 주제를 정하고, 그 주제에 대해서 너의 의견을 말해줘"

        message = message + ", 그리고 글자수는 " + length + " 로 작성해줘" 

        #gpt에 스크립트 전달
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        #gpt의 답변 반환
        return completion.choices[0].message.content
        