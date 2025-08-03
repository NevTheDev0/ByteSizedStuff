import { useEffect,useState } from "react";


function MyButton(){
    const[clicks,setClicks] = useState(0)
    const[timeLeft,setTimeLeft] = useState(10)
    const[isRunning, setIsRunning] = useState(false)
    const[hasFinished, setHasFinished] = useState(false);

    const startTest = () => {
        setClicks(0)
        setTimeLeft(10)
        setIsRunning(true)
        setHasFinished(false)
    }
    const reset = () => {
        setClicks(0)
        setTimeLeft(10)
        setIsRunning(false)
        setHasFinished(false)
    }
    const increment = () => {
        if(isRunning === true){
            setClicks(clicks + 1)
        }       
    }
    

    useEffect(() => {

        if(!isRunning) return;
        
        const interval = setInterval(() => {
            setTimeLeft(prev => {
                if(prev <= 1){
                    clearInterval(interval)
                    setIsRunning(false)
                    setHasFinished(true);
                    return 0;
                }
                return prev - 1;
            });
        },1000)
        return () => clearInterval(interval);
    }, [isRunning]);




    return(
        <div>
            <h1>Count: {clicks}</h1>
            {!isRunning && !hasFinished && (
                <button onClick={startTest}>Start Test</button>
            )}

            {isRunning && (
                <>
                    <p>Time left: {timeLeft}</p>
                    <button onClick={increment}>Click Me!</button>

                </>
            )}


            {!isRunning && hasFinished && (
                <>
                    <p>Total clicks:  {clicks}</p>
                    <p>CPS: {(clicks/10).toFixed(2)}</p>
                    <button onClick={reset}>Try again?</button>

                </>
            )}

        </div>

    );
}



export default MyButton