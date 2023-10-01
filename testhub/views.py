from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer


# Create your views here.
def index(request):
    """View function for home page"""

    return (render(request, 'index.html'))


def get_questions(request, question_id):
    """Method that get the questions from the data
        store the users response in a session
    """
    
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    
    #display nextbutton based on the question
    nextQuestion =Question.objects.filter(id__gt=question.id).order_by('id').first()
    #display prev button based on the question
    prevQuestion =Question.objects.filter(id__lt=question.id).order_by('-id').first()
    
    
    if request.method == 'POST':
        selected_answer_id = request.POST.get('selected_answer')
        selected_answer = get_object_or_404(Answer, pk=selected_answer_id)
        is_correct = selected_answer.is_correct
        
        #check if 'user_responses' not in session
        if 'user_responses' not in request.session:
            requestion.session['user_responses'] = {}
        
        request.session['user_responses'][question_id] = {
            'selected_answer_id': selected_answer_id,
            'is_correct': is_correct
        }
        
        
        if nextQuestion:
            return (redirect('get_questions_json', question_id=nextQuestion.id))
        else:
            
            return (render("Quiz completed"))
        
        
    
    return (render(request, 'quiz.html', {'question': question,
                                          'answers': answers,
                                          'prevQuestion': prevQuestion,
                                          'nextQuestion': nextQuestion}))
    
    
    
    
def review_quiz(request):
        """Method that display the quiz result"""
        
        #Get the user responses from the session
        user_responses = request.session.get('user_responses', {})
        
        
        total_score = 0
        for question_id, response_data in user_responses.items():
            is_correct = response.info.get('is_correct', False)
            if is_correct:
                total_score += 1
    
        return (render(request, 'review.html',
                   {
                       'user_responses': user_responses,
                       'total_score': total_score,
                   }))
        