package a11919434;

/**
 * Defines the various magic levels.
 * wizards have a magic level.
 * in order to be able to use specific spells a minimum magic level is necessary.
 * Note: the compiler generated default constructor may not be sufficient for your implementation
 */
public enum MagicLevel {
	NOOB(50,"*"),
	ADEPT(100,"**"),
	STUDENT(200,"***"),
	EXPERT(500,"****"),
	MASTER(1000,"*****");
	
	private int MP = 0;
	private String sign;
	MagicLevel(int MP,String sign){
		this.MP = MP;
		this.sign = sign;
	}
	public int toMana() {
		return MP;
	}
	@Override
	public String toString() {return sign;}
	
	
}