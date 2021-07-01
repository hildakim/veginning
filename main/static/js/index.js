
    //변수
    var sliderWrapper = document.getElementsByClassName("main-slider"),
        sliderContainer = document.getElementsByClassName('slider-container'),
        slides = document.getElementsByClassName('slide'),
        slideCount = slides.length, //슬라이드 개수
        currentIndex = 0, //현재 몇번째 슬라이드?
        topHeight = 0, //자식요소들 중 가장 높이가 큰 거 구할때 쓸것
        navPrev = document.getElementById('prev'),
        navNext = document.getElementById('next');

    //슬라이드의 높이 확인하여 부모의 높이로 지정
    function calculateTallestSlides(){
        for(var i = 0; i < slideCount; i++){
            if(slides[i].offsetHeight > topHeight){
                topHeight = slides[i].offsetHeight;
            }
        }
        sliderWrapper[0].style.height = topHeight +'px';
        sliderContainer[0].style.height = topHeight +'px';
    }

    // calculateTallestSlides();
    
    //슬라이드 가로 배열하기
    for(var i = 0; i < slideCount; i++){
        slides[i].style.left = i*100 + '%'; 
    }
    
    //슬라이드 이동 함수
    function goToSlide(idx){
        sliderContainer[0].style.left = idx * -100 + '%';
        sliderContainer[0].classList.add('animated');
        currentIndex = idx;

        updateNav();
    }

    //임의로..
    // sliderWrapper[0].style.height = 400 +'px';
    // sliderContainer[0].style.height = 400 +'px';
    
    //버튼 기능 업데이트 함수
    function updateNav(){
        //슬라이드 처음일때
        if(currentIndex == 0){
            navPrev.classList.add('disabled');
        } else{
            navPrev.classList.remove('disabled');
        }
        //슬라이드 끝일때
        if(currentIndex == slideCount-1){
            navNext.classList.add('disabled');
        } else {
            navNext.classList.remove('disabled');
        }
    }


    //버튼을 클릭하면 슬라이드 이동
    navPrev.addEventListener('click', function(event){
        event.preventDefault(0); //a의 기본 기능 막기
        goToSlide(currentIndex - 1);
    });
    navNext.addEventListener('click', function(evevt){
        event.preventDefault(0); 
        goToSlide(currentIndex + 1);
    });

    //첫번째 슬라이드 먼저 보이도록 하기(prev버튼 없어야하기때문에)
    goToSlide(0);
