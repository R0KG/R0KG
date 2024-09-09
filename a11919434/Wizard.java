package a11919434;

import java.util.*;

import javax.management.RuntimeErrorException;
/**
 * Wizard class objects are the primary actors in the game. They can use and trade items, provide
 * magic energy, cast spells and also are affected be various magical effects.
 */
public class Wizard implements MagicSource, Trader, MagicEffectRealization {
	/**
	 * Not null not empty
	 */
	private String name; 
	/**
	 * Not null
	 * */
	private MagicLevel level;
	/**
	 * Not negative
	 */
	private int basicHP;
	/**
	 * Not negative; defaults to basicHP
	 */
	private int HP;
	/**
	 * Not less than the manapoints associated with the magic level
	 */
	private int basicMP;
	/**
	 * Not negative; defaults to basicMP
	 */
	private int MP;
	/**
	 * Not negative
	 */
	private int money;
	/**
	 * Not null, may be empty; use HashSet for instantiation
	 */
	private Set<Spell> knownSpells;
	/**
	 * Not null, may be empty; use HashSet for instantiation
	 */
	private Set<AttackingSpell> protectedFrom;
	/**
	 * Not negative
	 */
	private int carryingCapacity;
	/**
	 * Not null, may be empty, use HashSet for instantiation, total weight of inventory
	 * may never exceed carryingCapacity
	 */
	private Set<Tradeable> inventory;

	/**
	 * @param name name
	 * @param level the magic level (proficiency needed to 	cast spells)
	 * @param basicHP base for percentage health calculations
	 * @param HP current health 
	 * @param basicMP base for percentage mana calculations
	 * @param MP current mana
	 * @param money current money
	 * @param knownSpells set of known spells
	 * @param protectedFrom set of spells the object is protected against
	 * @param carryingCapacity maximum carrying capacity
	 * @param inventory set of items the object is currently carrying
	 */
	public Wizard(String name, MagicLevel level, int basicHP, int HP, int basicMP, int MP, int money,
			Set<Spell> knownSpells, Set<AttackingSpell> protectedFrom, int carryingCapacity,
			Set<Tradeable> inventory) 
	{
		if(name == null || name.isEmpty() || level == null || basicHP < 0 || HP < 0 || basicMP < level.toMana() || MP < 0 || money < 0 || knownSpells == null || protectedFrom == null || carryingCapacity < 0 || inventory == null) throw new IllegalArgumentException("Error const Wizard");
		this.name = name;
		this.level = level;
		this.basicHP = basicHP;
		this.HP = HP;
		this.basicMP = basicMP;
		this.MP = MP;
		this.money = money;
	    this.knownSpells = new HashSet<>(knownSpells);
		this.protectedFrom = new HashSet<>(protectedFrom);
		this.carryingCapacity = carryingCapacity;
		this.inventory = new HashSet<>(inventory);
		int temp = 0;
		for(Tradeable item : this.inventory) {
			temp+= item.getWeight();
		}
		if(temp > carryingCapacity ) {
			throw new IllegalArgumentException();
		}
	}
	public Wizard(String name, MagicLevel level, int basicHP,int basicMP,int money,
			Set<Spell> knownSpells, Set<AttackingSpell> protectedFrom, int carryingCapacity,
			Set<Tradeable> inventory) 
	{
		if(name == null || name.isEmpty() || level == null || basicHP < 0  || basicMP < level.toMana()  || money < 0 || knownSpells == null || protectedFrom == null || carryingCapacity < 0 || inventory == null) throw new IllegalArgumentException("Error const Wizard");
		this.name = name;
		this.level = level;
		this.basicHP = basicHP;
		this.HP = basicHP;
		this.basicMP = basicMP;
		this.MP = basicMP;
		this.money = money;
	    this.knownSpells = new HashSet<>(knownSpells);
		this.protectedFrom = new HashSet<>(protectedFrom);
		this.carryingCapacity = carryingCapacity;
		this.inventory = new HashSet<>(inventory);
		int temp = 0;
		for(Tradeable item : this.inventory) {
			temp+= item.getWeight();
		}
		if(temp > carryingCapacity ) {
			throw new IllegalArgumentException();
		}
	}

	/**
	 * Return true, if HP is 0, false otherwise
	 * @return true, if HP is 0, false otherwise
	 */
	public boolean isDead() {
		return (HP == 0);
	}  
	public Set<AttackingSpell> getProtectedFrom(){
		return protectedFrom;
	}
	public String getName(){
		return name;
	}
	public int getBasicMP(){
		return basicMP;
	}
	public int getBasicHP(){
		return basicHP;
	}
	public MagicLevel getLevel(){
		return level;
	}
	public Set<Tradeable> getInventory(){
		return inventory;
	}
	public int getMoney() {
		return money;
	}
	public Set<Spell> getKnownSpells(){
		return knownSpells;
	}
	public int getCarryingCapacity() {
		return carryingCapacity;
	}
	  
	/**
	 * Calculates and returns the total weight of all the items in the inventory
	 * @return total weight of all items in inventory
	 */
	public int inventoryTotalWeight() {
		int temp = 0;
		for(Tradeable item : inventory) {
			temp+= item.getWeight();
		}
		return temp;
	}
	  
	/**
	 * If spell is null, IllegalArgumentException has to be thrown;
	 * if wizard is dead (isDead) no action can be taken and false is returned;
	 * add spell to the set of knownSpells;
	 * returns true, if insertion was successful, false otherwise.
	 * @param s spell to be learned
	 * @return true, if insertion was successful, false otherwise.
	 */
	public boolean learn(Spell s) {
		if(s == null) throw new IllegalArgumentException("Error with learn function");
		if(isDead()) return false;
		if(knownSpells.add(s)) return true;
		return false;
	}
	  
	/**
	 * If spell is null, IllegalArgumentException has to be thrown;
	 * if wizard is dead (isDead) no action can be taken and false is returned;
	 * remove spell from the set of knownSpells;
	 * returns true if removal was successful, false otherwise.
	 * @param s spell that the object is about to learn
	 * @return true, if removal was successful, false otherwise.
	 */
	public boolean forget(Spell s) {
		if(s == null) throw new IllegalArgumentException("Error with learn function");
		if(isDead()) return false;
		if(knownSpells.remove(s)) return true;
		return false;
	}
	
	/**
	 * If s or target is null, IllegalArgumentException has to be thrown;
	 * if wizard is dead (isDead) no action can be taken and false is returned;
	 * if wizard does not know the spell, false is returned;
	 * call cast on s with this as source and parameter target as target
	 * return true, if cast was called;
	 * @param s spell to be cast
	 * @param target target of the spell to cast
	 * @return true, if cast was called, false otherwise;
	 */
	public boolean castSpell(Spell s, MagicEffectRealization target) {
		if(s == null || target == null) throw new IllegalArgumentException("Error with learn function");
		if(isDead()) return false;
		if(!knownSpells.contains(s)) return false;
		s.cast(this, target);
		return true;
	}
	  
	/**
	 * If this object's knownSpells is empty, return false
	 * otherwise choose a random spell from knownSpells and delegate to
	 * castSpell(Spell, MagicEffectRealization)
	 * @param target target of the spell to cast
	 * @return false, if the object does not know a spell, otherwise the
	 * result of the delegation to castSpell
	 */
	public boolean castRandomSpell(MagicEffectRealization target) {
		if(target == null) throw new IllegalArgumentException("Error with learn function");
		if(knownSpells.isEmpty()) return false;
		List<Spell> spellsList = new ArrayList<Spell>(knownSpells);
		Random rand = new Random();
		int randIndex = rand.nextInt(spellsList.size());
		Spell randomSpell = spellsList.get(randIndex);
		return castSpell(randomSpell, target);
	}
	  
	/**
	 * If item or target is null, IllegalArgumentException has to be thrown;
	 * if wizard is dead (isDead) no action can be taken and false is returned;
	 * if wizard does not possess the item, false is returned;
	 * call useOn on the item with parameter target as target;
	 * return true, if useOn was called.
	 * @param item item to be used
	 * @param target target on which item is to be used on
	 * @return true, if useOn was called, false otherwise
	 */
	public boolean useItem(Tradeable item, MagicEffectRealization target) {
		if(item == null || target == null) throw new IllegalArgumentException("Error with learn function");
		if(isDead()) return false;
		if(!inventory.contains(item)) return false;
		item.useOn(target);
		return true;
	}

	/**
	 * If this object's inventory is empty, return false;
	 * otherwise choose a random item from inventory and delegate to
	 * useItem(Tradeable, MagicEffectRealization).
	 * @param target target on which item is to be used on
	 * @return false, if the object does not possess any item, otherwise the
	 * result of the delegation to useItem
	 */
	public boolean useRandomItem(MagicEffectRealization target) {
		if(target == null) throw new IllegalArgumentException("Error with learn function");
		if(inventory.isEmpty()) return false;
		List<Tradeable> itemList = new ArrayList<Tradeable>(inventory);
		Random rand = new Random();
		int randIndex = rand.nextInt(itemList.size());
		Tradeable randomItem = itemList.get(randIndex);
		return useItem(randomItem, target);
	}
	  
	/**
	 * If item or target is null, IllegalArgumentException has to be thrown;
	 * if wizard is dead (isDead), no action can be taken and false is returned;
	 * call purchase on the item with this as seller and target as buyer;
	 * return true, if purchase was called successfully (returned true), false
	 * otherwise.
	 * @param item item to be sold
	 * @param target object the item is sold to (buyer)
	 * @return true, if purchase was called successfully (returned true), false
	 * otherwise.
	 */ 
	public boolean sellItem(Tradeable item, Trader target) {
		if(item == null || target == null) throw new IllegalArgumentException("Error with learn function");
		if(isDead()) return false;
		if(item.purchase(this, target)) return true;
		return false;
		
	}

	/**
	 * If this object's inventory is empty, return false,
	 * otherwise choose a random item from inventory and delegate to
	 * sellItem(Tradeable, MagicEffectRealization).
	 * @param target object the item is sold to (buyer)
	 * @return false, if the object does not possess any item, otherwise the
	 * result of the delegation to sellItem
	 */
	public boolean sellRandomItem(Trader target) {
		if(target == null) throw new IllegalArgumentException("Error with learn function");
		if(inventory.isEmpty()) return false;
		List<Tradeable> itemList = new ArrayList<Tradeable>(inventory);
		Random rand = new Random();
		int randIndex = rand.nextInt(itemList.size());
		Tradeable randomItem = itemList.get(randIndex);
		return sellItem(randomItem, target);
	}

	/**
	 * Returns a string in the format
	 * "['name'('level'): 'HP'/'basicHP' 'MP'/'basicMP'; 'money' 'KnutOrKnuts'; knows 'knownSpells'; carries 'inventory']";
	 * where 'level' is the asterisks representation of the level
	 * (see MagicLevel.toString) and 'knownSpells' and 'inventory' use
	 * the default toString method of Java Set; 'KnutOrKnuts' is Knut
	 * if 'money' is 1, Knuts otherwise.
	 * E.g. [Ignatius(**): 70/100 100/150; 72 Knuts; knows [[Episkey(*): 5 mana; +20 HP], [Confringo: 10 mana; -20 HP]]; carries []]
	 * @return "['name'('level'): 'HP'/'basicHP' 'MP'/'basicMP'; 'money' 'KnutOrKnuts'; knows 'knownSpells'; carries 'inventory']"
	 */ 
	@Override
	public String toString() {
		String temp = "[" + name + "("+ level.toString() + "): " ;
		temp += HP + "/" + basicHP + " " + MP + "/" + basicMP +"; ";
		temp += money;
		temp += (money == 1) ? " Knut;" : " Knuts;";
		temp += " knows " + knownSpells.toString() + "; carries " + inventory.toString() + "]";	
		return temp;
		
	}
	
	//MagicSource Interface
	
	/**
	 * If wizard is dead (isDead) no action can be taken and false is returned:
	 * check if level is at least levelNeeded, return false otherwise;
	 * if MP is less than manaAmount return false;
	 * subtract manaAmount from MP and return true.
	 * @param levelNeeded minimum magic level needed for the action 
	 * @param manaAmount amount of mana needed for the action 
	 * @return true, if mana can be successfully provided, false otherwise
	 */
	@Override
	public boolean provideMana(MagicLevel levelNeeded, int manaAmount) {
		if(levelNeeded == null || manaAmount < 0) throw new IllegalArgumentException("Error with learn function");
		if(isDead()) return false;
		if(level.toString().compareTo(levelNeeded.toString()) < 0) return false;
		if(MP < manaAmount) return false;
		MP -= manaAmount;
		return true;
	}

	//Trader Interface

	/**
	 * Return true, if the item is in the inventory, false otherwise
	 * @param item object is tested, if it possesses this item
	 * @return true, if the item is in the inventory, false otherwise
	 */
	@Override
	public boolean possesses(Tradeable item) {
		if(item == null) throw new IllegalArgumentException();
		if(inventory.contains(item)) return true;
		return false;
	}

	/**
	 * Return true, if money is greater than or equal to amount, false otherwise
	 * @param amount object is tested, if it owns enough money to pay this amount
	 * @return true, if money is greater than or equal to amount, false otherwise
	 */
	@Override
	public boolean canAfford(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		return (money >= amount);
	}

	/**
	 * Return true, if inventoryTotalWeight+weight is less than or equal to carryingCapacity, false otherwise
	 * @param weight test, if this weight can be added to object's inventory, without exceeding the
	 * carryingCapacity
	 * @return true, if inventoryTotalWeight+weight is less than or equal to carryingCapacity, false otherwise
	 */
	@Override
	public boolean hasCapacity(int weight) {
		if(weight < 0) throw new IllegalArgumentException();
		return ((inventoryTotalWeight() + weight) <= carryingCapacity);
	}

	/**
	 * If wizard is dead (isDead) no action can be taken and false is returned;
	 * if this owns enough money deduct amount from money and return true,
	 * return false otherwise
	 * @param amount to be payed
	 * @return true, if payment succeeds, false otherwise
	 */
	@Override
	public boolean pay(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		if(isDead()) return false;
		if(money >= amount) {
			money -= amount;
			return true;
		}
		return false;
	}
	public int getMP() {
		return MP;
	}
	public int getHP() {
		return HP;
	}
	    
	/**
	 * If wizard is dead (isDead), no action can be taken and false is returned;
	 * add amount to this object's money and return true.
	 * @param amount amount to be received
	 * @return true, if reception succeeds, false otherwise 
	 */
	@Override
	public boolean earn(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		if(isDead()) return false;
		money += amount;
		return true;
		

	}
	    
	/**
	 * Add item to inventory if carryingCapacity is sufficient.
	 * returns true, if item is successfully added, false otherwise
	 * (carrying capacity exceeded or item is already in the inventory)
	 * @param item item to be added to object's inventory
	 * @return true. if item is successfully added, false otherwise
	 */
	@Override
	public boolean addToInventory(Tradeable item) {
		if(item == null) throw new IllegalArgumentException();
		if(hasCapacity(item.getWeight())) {
			if(inventory.add(item)) return true;
			return false;
			
		}
		return false;
	}

	/**
	 * Remove item from inventory.
	 * returns true, if item is successfully removed, false otherwise
	 * (item not in the inventory).
	 * @param item item to be removed from object's inventory
	 * @return true, if item is successfully removed, false otherwise
	 */
	@Override
	public boolean removeFromInventory(Tradeable item) {
		if(item == null) throw new IllegalArgumentException();
		if(inventory.remove(item)) return true;
		return false;
	}
	
	/**
	 * Returns true, if this object's HP are not 0 (alive wizard).
	 * @return true, if the object is alive
	 */
	@Override
	public boolean canSteal() {
		return (!isDead());
	}
	
	/**
	 * If thief is null, IllegalArgumentException has to be thrown;
	 * if thief cannot steal (canSteal returns false) no action can be taken
	 * and false is returned;
	 * returns false if, the object's inventory is empty;
	 * otherwise transfers a random item from the this object's inventory into
	 * the thief's inventory;
	 * if the thief's inventory has not enough capacity, the object just vanishes
	 * and false is returned;
	 * returns true, if theft was successful.
	 * @param thief object that is stealing the item from the this-object. 
	 * @return true, if theft was successful
	 */
	@Override
	public boolean steal(Trader thief) {
		if(thief == null) throw new IllegalArgumentException("Error with steal func");
		if(!canSteal()) return false;
		if(inventory.isEmpty()) return false;
		List<Tradeable> inventList = new ArrayList<Tradeable>(inventory);
		Random rand = new Random();
		int randIndex = rand.nextInt(inventList.size());
		Tradeable randItem = inventList.get(randIndex);
		if(thief.hasCapacity(randItem.getWeight())) {
			if(thief.addToInventory(randItem) && this.removeFromInventory(randItem)) return true;
		}
		return false;
	}

	/**
	 * Returns true if, this object's HP are 0 (dead wizard)
	 * @return true if the object is dead
	 */
	@Override
	public boolean isLootable() {
		return (isDead());
	}

	/**
	 * Returns true if this object's HP are not 0 (alive wizard)
	 * @return true, if the object is alive
	 */
	@Override
	public boolean canLoot() {
		return (!isDead());
	}
	
	/**
	 * Of looter is null, IllegalArgumentException has to be thrown;
	 * if looter cannot loot (canLoot returns false), no action can be taken
	 * and false is returned;
	 * if the this object can be looted (isLootable), transfer all the items
	 * in the object's inventory into the looter's inventory;
	 * items that don't fit in the looter's inventory because of the weight
	 * limitation just vanish.
	 * returns true, if at least one item was successfully transferred, false
	 * otherwise.
	 * @param looter object that is looting this-object.
	 * @return true, if looting was successful, false otherwise
	 */
	@Override
	public boolean loot(Trader looter) {
		if(looter == null) throw new IllegalArgumentException("Error loot func");
		if(!canLoot()) return false;
		if(isLootable()) {
			boolean possible_transfer = false;
			for(Tradeable item : inventory) {
				if(looter.addToInventory(item) && removeFromInventory(item)) possible_transfer = true;
			}
		if(possible_transfer) return true;
		}
		return false;
	}
	  
	//MagicEffectRealization Interface
	
	/**
	 * Reduce the object's HP by amount ensuring however that HP does not
	 * become negative.
	 * @param amount amount to be deducted from health 
	 */
	@Override
	public void takeDamage(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		HP -= amount;
		if(HP < 0) {
			HP = 0;
		}
	}
	    
	/**
	 * Reduce the object's HP by the percentage given of the object's basic
	 * HP value ensuring however, that HP does not become negative.
	 * Do calculations in double truncating to int only for the assignment
	 * @param percentage percentage of damage done
	 */
	@Override
	public void takeDamagePercent(int percentage) {
		if(percentage < 0 || percentage > 100) throw new IllegalArgumentException();
		double damage = basicHP * ((double)percentage / 100.0);
		HP = Math.max(0,(HP - (int)damage));
	}
	    
	/**
	 * Reduce the object's MP by amount ensuring however that MP does not
	 * become negative.
	 * @param amount amount to be deducted from mana 
	 */
	@Override
	public void weakenMagic(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		MP -= amount;
		if(MP < 0) {
			MP = 0;
		}
	}
	  
	/**
	 * Reduce the object's MP by the percentage given of the object's basic
	 * MP value ensuring however, that MP does not become negative.
	 * Do calculations in double truncating to int only for the assignment
	 * @param percentage percentage of damage done
	 */
	@Override
	public void weakenMagicPercent(int percentage) {
		if(percentage < 0 || percentage > 100) throw new IllegalArgumentException();
		double damage = basicMP * ((double)percentage / 100.0);
		MP = Math.max(0,(MP -(int)damage));
	}
	  
	/**
	 * Increase the object's HP by the amount given.
	 * @param amount amount to increase health
	 */
	@Override
	public void heal(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		HP += amount;
	}
	    
	/**
	 * Increase the object's HP by the percentage given of the object's
	 * basic HP. Do calculations in double truncating to int only for
	 * the assignment
	 * @param percentage percentage of healing done
	 */
	@Override
	public void healPercent(int percentage) {
		if(percentage < 0 || percentage > 100) throw new IllegalArgumentException();
		double heal = basicHP * ((double)percentage / 100.0);
		HP = HP + (int)heal;
	}

	/**
	 * Increase the object's MP by the amount given.
	 * @param amount amount to increase mana
	 */
	@Override
	public void enforceMagic(int amount) {
		if(amount < 0) throw new IllegalArgumentException();
		MP += amount;	
	}
	  
	/**
	 * Increase the object's MP by the percentage given of the object's
	 * basic MP. Do calculations in double truncating to int only for
	 * the assignment
	 * @param percentage percentage of mana increase
	 */
	@Override
	public void enforceMagicPercent(int percentage) {
		if(percentage < 0 || percentage > 100) throw new IllegalArgumentException();
		double mana = basicMP * ((double)percentage / 100.0);
		MP = MP + (int)mana;
	}
	    
	/**
	 * Return true, if s is contained in instance variable protectedFrom
	 * @param s spell that is tested for
	 * @return true, if object is protected against spell s, false otherwise
	 */
	@Override
	public boolean isProtected(Spell s) {
		if(s == null) throw new IllegalArgumentException();
		return (protectedFrom.contains(s));
	}
	    
	/**
	 * Add all spells from attacks to instance variable protectedFrom
	 * @param attacks spells against which protection is provided
	 */
	@Override
	public void setProtection(Set<AttackingSpell> attacks) {
		if(attacks == null) throw new IllegalArgumentException();
		protectedFrom.addAll(attacks);
	}

	/**
	 * Remove all spells from attacks from instance variable protectedFrom
	 * @param attacks spells against which protection is removed 
	 */
	@Override
	public void removeProtection(Set<AttackingSpell> attacks) {
		if(attacks == null) throw new IllegalArgumentException();
		protectedFrom.removeAll(attacks);
	}
}