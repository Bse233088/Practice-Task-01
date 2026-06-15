import static org.junit.Assert.*;
import org.junit.Test;
public class CalculatorTest{
    @Test
    public void testAddition(){
        Calculator clac=new Calculator();
        int result=calc.add(5,3);
        assertEquals(8,result);
    }
}
